#!/usr/bin/python3
"""Reunir as fontes do pacote de André e atualizar os dois PDFs."""

from pathlib import Path
import csv
import re
import subprocess
import sys

BASE = Path(__file__).resolve().parent
RENDERER = BASE.parent.parent / 'gpt' / 'gerar_pdf_reuniao.py'
SUFFIX = '2a_reuniao_2026-10-29'
SOURCES = [
    ('Começar aqui', f'00_comecar_Andre_{SUFFIX}.md'),
    ('Requisitos e regulamento', f'01_requisitos_{SUFFIX}.md'),
    ('Arquitetura e pesquisa técnica', f'02_arquitetura_pesquisa_{SUFFIX}.md'),
    ('Empresas e contactos', f'03_empresas_contactos_{SUFFIX}.md'),
    ('Plano de execução de André', f'04_execucao_Andre_{SUFFIX}.md'),
    ('Mensagens e pauta do próximo encontro', f'05_mensagens_pauta_{SUFFIX}.md'),
    ('Fontes do regulamento', f'fontes_regulamento_{SUFFIX}.md'),
]


def main():
    missing = [name for _, name in SOURCES if not (BASE / name).is_file()]
    if missing:
        raise SystemExit('Faltam documentos: ' + ', '.join(missing))
    content = [
        '# UAS 2027 — 2.ª reunião — 29/10/2026 — Dossiê de André',
        '',
        'Preparação de Software/Comunicações: pesquisa realizada, propostas para decisão, interfaces e seguimento.',
        '',
        '**Estado:** preparação documental concluída; decisões da equipa e evidências de ensaio mantêm estados próprios. As fontes estão ligadas nos respetivos capítulos.',
        '',
    ]
    for index, (title, name) in enumerate(SOURCES, 1):
        content.extend([f'## Parte {index} — {title}', ''])
        lines = (BASE / name).read_text(encoding='utf-8').splitlines()
        if lines and lines[0].startswith('# '):
            lines = lines[1:]
        in_fence = False
        for line in lines:
            if line.strip().startswith('```'):
                in_fence = not in_fence
            if not in_fence and re.match(r'^#{1,5} ', line):
                line = '#' + line
            content.append(line)
        content.extend(['', '---', ''])
    # Uma ligação por linha preserva no PDF os destinos das fontes que apareçam
    # juntas em células ou parágrafos dos documentos originais.
    urls = {}
    for _, name in SOURCES:
        text = (BASE / name).read_text(encoding='utf-8')
        for label, uri in re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', text):
            urls.setdefault(uri, label)
    for path in sorted(BASE.glob('*.csv')):
        with path.open(encoding='utf-8-sig', newline='') as source:
            for row in csv.DictReader(source):
                for value in row.values():
                    for uri in re.findall(r'https?://[^\s<>]+', value or ''):
                        uri = uri.rstrip('.,;)')
                        urls.setdefault(uri, 'Fonte na folha ' + path.stem)
    catalogue = [
        '# UAS 2027 — 2.ª reunião — 29/10/2026 — Fontes da pesquisa',
        '',
        'Índice das fontes citadas nos documentos e folhas de trabalho. Cada entrada tem uma ligação própria no PDF. As afirmações e os contextos de utilização permanecem nos respetivos capítulos.',
        '',
    ]
    catalogue.extend(f'- [F{i:02} — {label}]({uri})' for i, (uri, label) in enumerate(urls.items(), 1))
    catalogue_path = BASE / f'fontes_pesquisa_{SUFFIX}.md'
    catalogue_path.write_text('\n'.join(catalogue) + '\n', encoding='utf-8')
    content.extend(['## Parte 8 — Índice das fontes externas', '', *catalogue[1:], ''])
    dossier = BASE / f'dossie_Andre_{SUFFIX}.md'
    dossier.write_text('\n'.join(content), encoding='utf-8')
    for source, destination in [
        (BASE / SOURCES[0][1], BASE / f'briefing_Andre_{SUFFIX}.pdf'),
        (dossier, BASE / f'dossie_Andre_{SUFFIX}.pdf'),
    ]:
        subprocess.run([sys.executable, str(RENDERER), str(source), str(destination)], check=True)


if __name__ == '__main__':
    main()
