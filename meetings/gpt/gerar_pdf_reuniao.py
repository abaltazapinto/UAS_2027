#!/usr/bin/python3
"""Renderizar atas Markdown em PDF: /usr/bin/python3 gerar_pdf_reuniao.py fonte.md destino.pdf."""

import argparse
import html
import re
from pathlib import Path

import cairo
import gi

gi.require_version("Pango", "1.0")
gi.require_version("PangoCairo", "1.0")
from gi.repository import Pango, PangoCairo


WIDTH, HEIGHT = 595.276, 841.890
LEFT, RIGHT, TOP, BOTTOM = 43, 43, 57, 786
INK, MUTED, BLUE = (0.14, 0.18, 0.23), (0.40, 0.46, 0.52), (0.08, 0.26, 0.38)


def markup(value):
    """Subset deliberadamente pequeno de Markdown, com escape de XML."""
    value = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", value)
    value = html.escape(value)
    value = re.sub(r"`([^`]+)`", r'<span font_family="DejaVu Sans Mono">\1</span>', value)
    value = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    return value


class PDF:
    def __init__(self, destination, title):
        self.surface = cairo.PDFSurface(str(destination), WIDTH, HEIGHT)
        self.surface.set_metadata(cairo.PDF_METADATA_TITLE, title)
        self.surface.set_metadata(cairo.PDF_METADATA_AUTHOR, "UAS 2027")
        self.ctx = cairo.Context(self.surface)
        self.title, self.page, self.y = title, 0, TOP
        self.new_page()

    def layout(self, value, width, size=9.8, bold=False, literal=False):
        layout = PangoCairo.create_layout(self.ctx)
        font = Pango.FontDescription("DejaVu Sans")
        font.set_absolute_size(size * Pango.SCALE)
        if bold:
            font.set_weight(Pango.Weight.BOLD)
        layout.set_font_description(font)
        layout.set_width(int(width * Pango.SCALE))
        layout.set_wrap(Pango.WrapMode.WORD_CHAR)
        layout.set_spacing(int(3.0 * Pango.SCALE))
        if literal:
            layout.set_text(value, -1)
        else:
            layout.set_markup(markup(value), -1)
        links = re.findall(r"\[[^\]]+\]\((https?://[^)]+)\)", value)
        layout.pdf_uri = links[0] if len(links) == 1 else None
        return layout

    @staticmethod
    def height(layout):
        return layout.get_size()[1] / Pango.SCALE

    @staticmethod
    def lines(layout):
        result, iterator = [], layout.get_iter()
        while True:
            rectangle = iterator.get_line_extents()[1]
            result.append((rectangle.y / Pango.SCALE, (rectangle.y + rectangle.height) / Pango.SCALE))
            if not iterator.next_line():
                break
        return result

    def draw(self, layout, x, y, color=INK):
        self.ctx.set_source_rgb(*color)
        self.ctx.move_to(x, y)
        tagged = False
        if getattr(layout, "pdf_uri", None):
            clip_left, clip_top, clip_right, clip_bottom = self.ctx.clip_extents()
            width, height = (v / Pango.SCALE for v in layout.get_size())
            left, top = max(x, clip_left), max(y, clip_top)
            right, bottom = min(x + width, clip_right), min(y + height, clip_bottom)
            if right > left and bottom > top:
                uri = layout.pdf_uri.replace("\\", "\\\\").replace("'", "\\'")
                self.ctx.tag_begin(cairo.TAG_LINK,
                                   f"uri='{uri}' rect=[{left} {top} {right-left} {bottom-top}]")
                tagged = True
        PangoCairo.show_layout(self.ctx, layout)
        if tagged:
            self.ctx.tag_end(cairo.TAG_LINK)

    def new_page(self):
        if self.page:
            self.surface.show_page()
        self.page += 1
        self.y = TOP
        header = self.layout(self.title, WIDTH - LEFT - RIGHT, size=7.8, literal=True)
        header.set_ellipsize(Pango.EllipsizeMode.END)
        header.set_height(-1)
        self.draw(header, LEFT, 25, MUTED)
        self.ctx.set_source_rgb(0.80, 0.85, 0.88)
        self.ctx.set_line_width(0.6)
        self.ctx.move_to(LEFT, 44)
        self.ctx.line_to(WIDTH - RIGHT, 44)
        self.ctx.stroke()
        self.draw(self.layout("UAS 2027 · Registo de reunião", 420, size=7.5), LEFT, 811, MUTED)
        self.draw(self.layout(str(self.page), 30, size=7.5), WIDTH - RIGHT - 20, 811, MUTED)

    def ensure(self, height):
        if self.y + height > BOTTOM:
            self.new_page()

    def paragraph(self, value, size=9.8, bold=False, indent=0, after=7, color=INK):
        layout = self.layout(value, WIDTH - LEFT - RIGHT - indent, size, bold)
        lines, first = self.lines(layout), 0
        while first < len(lines):
            start = lines[first][0]
            available = BOTTOM - self.y
            last = first
            while last < len(lines) and lines[last][1] - start <= available:
                last += 1
            if last == first:
                self.new_page()
                continue
            end = lines[last - 1][1]
            self.ctx.save()
            self.ctx.rectangle(LEFT + indent, self.y, WIDTH - LEFT - RIGHT - indent, end - start + 0.2)
            self.ctx.clip()
            self.draw(layout, LEFT + indent, self.y - start, color)
            self.ctx.restore()
            self.y += end - start
            first = last
            if first < len(lines):
                self.new_page()
        self.y += after

    def heading(self, value, level):
        size = {1: 20, 2: 13.8, 3: 11.2}.get(level, 10.2)
        height = self.height(self.layout(value, WIDTH - LEFT - RIGHT, size, True))
        self.ensure(height + 45)
        self.y += 5 if level == 1 else 9
        self.paragraph(value, size, True, after=9, color=BLUE)

    def table(self, rows):
        count = max(map(len, rows))
        if count == 2:
            weights = [0.29, 0.71]
        elif count == 3:
            weights = [0.23, 0.48, 0.29]
        elif count == 4:
            weights = [0.20, 0.40, 0.20, 0.20]
        elif count == 5:
            weights = [0.18, 0.34, 0.16, 0.16, 0.16]
        else:
            weights = [1 / count] * count
        widths = [(WIDTH - LEFT - RIGHT) * w for w in weights]

        def prepare(row, is_header=False):
            return [self.layout(row[i] if i < len(row) else "", width - 12, 8.4, is_header)
                    for i, width in enumerate(widths)]

        header = prepare(rows[0], True)
        header_height = max(map(self.height, header)) + 13

        def band(layouts, offset, height, is_header=False, alternate=False):
            x = LEFT
            fill = (0.88, 0.93, 0.96) if is_header else ((0.96, 0.97, 0.98) if alternate else (1, 1, 1))
            for width, layout in zip(widths, layouts):
                self.ctx.set_source_rgb(*fill)
                self.ctx.rectangle(x, self.y, width, height)
                self.ctx.fill()
                self.ctx.save()
                self.ctx.rectangle(x + 5, self.y + 3, width - 10, height - 6)
                self.ctx.clip()
                self.draw(layout, x + 6, self.y + 6 - offset, BLUE if is_header else INK)
                self.ctx.restore()
                self.ctx.set_source_rgb(0.80, 0.85, 0.88)
                self.ctx.set_line_width(0.35)
                self.ctx.rectangle(x, self.y, width, height)
                self.ctx.stroke()
                x += width
            self.y += height

        self.ensure(header_height + 35)
        band(header, 0, header_height, True)
        for row_number, row in enumerate(rows[1:]):
            layouts = prepare(row)
            full = max(map(self.height, layouts))
            if full + 13 <= BOTTOM - TOP - header_height and self.y + full + 13 > BOTTOM:
                self.new_page()
                band(header, 0, header_height, True)
            offset = 0
            while offset < full:
                available = BOTTOM - self.y - 13
                if available < 20:
                    self.new_page()
                    band(header, 0, header_height, True)
                    continue
                end = min(full, offset + available)
                # Move a split to a shared blank between lines, avoiding clipped glyphs.
                intervals = [(a, b) for layout in layouts for a, b in self.lines(layout)]
                while end < full:
                    crossing = [a for a, b in intervals if a < end < b]
                    if not crossing:
                        break
                    end = min(crossing)
                if end <= offset:
                    raise ValueError("Linha de tabela maior que a área útil da página")
                band(layouts, offset, end - offset + 13, alternate=row_number % 2 == 1)
                offset = end
                if offset < full:
                    self.new_page()
                    band(header, 0, header_height, True)
        self.y += 9

    def render(self, source):
        lines, index, fenced = source.splitlines(), 0, False
        while index < len(lines):
            line = lines[index].strip()
            index += 1
            if not line:
                continue
            if line.startswith("```"):
                fenced = not fenced
                continue
            if line.startswith("|") and not fenced:
                rows = []
                while True:
                    cells = [cell.strip() for cell in line.strip("|").split("|")]
                    if not all(re.fullmatch(r":?-+:?", cell) for cell in cells):
                        rows.append(cells)
                    if index >= len(lines) or not lines[index].strip().startswith("|"):
                        break
                    line = lines[index].strip()
                    index += 1
                if rows:
                    self.table(rows)
            elif match := re.match(r"^(#{1,6})\s+(.+)", line):
                self.heading(match[2], len(match[1]))
            elif re.fullmatch(r"[-*_]{3,}", line):
                self.y += 5
            elif line.startswith(">"):
                self.paragraph(line.lstrip("> "), indent=10, color=BLUE)
            else:
                if line.startswith(("- ", "* ")):
                    line = "• " + line[2:]
                if fenced:
                    line = "`" + line + "`"
                self.paragraph(line)
        self.surface.finish()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    source = args.source.read_text(encoding="utf-8")
    title = next((line[2:].strip() for line in source.splitlines() if line.startswith("# ")), args.source.stem)
    args.destination.parent.mkdir(parents=True, exist_ok=True)
    document = PDF(args.destination, title)
    document.render(source)
    print(f"{args.destination} — {document.page} páginas")


if __name__ == "__main__":
    main()
