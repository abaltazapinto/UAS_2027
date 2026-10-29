# UAS 2027 — Reuniões

## Registos

| Reunião | Data | Documentação |
|---|---|---|
| 1.ª reunião — recrutamento e apresentação | 13/10/2026 | [Resumo](1a_Reuniao/resumo_1a_reuniao.md) |
| 2.ª reunião | 29/10/2026 | [Resumo detalhado](2a_Reuniao%2029-10-26/resumo_2a_reuniao_2026-10-29.md) · [PDF](2a_Reuniao%2029-10-26/resumo_2a_reuniao_2026-10-29.pdf) · [Preparação e trabalho de André](2a_Reuniao%2029-10-26/preparacao_Andre_2a_reuniao_2026-10-29/00_comecar_Andre_2a_reuniao_2026-10-29.md) |

## Convenção para as próximas reuniões

O número e a data devem acompanhar cada reunião nas pastas, nos nomes dos documentos e nos títulos internos.

```text
meetings/
  <numero>a_Reuniao DD-MM-AA/
    resumo_<numero>a_reuniao_AAAA-MM-DD.md
    resumo_<numero>a_reuniao_AAAA-MM-DD.pdf
    transcricao/
      <numero>a_Reuniao_AAAA-MM-DD_transcricao_automatica.srt
```

Título interno: **UAS 2027 — <número>.ª reunião — DD/MM/AAAA**.

A pasta da 2.ª reunião mantém o nome escolhido: `2a_Reuniao 29-10-26`. Os registos antigos são preservados. As próximas pastas só devem receber uma data depois de esta estar confirmada.

Cada resumo deve identificar as equipas e os responsáveis que ficaram definidos, as decisões, as tarefas e os prazos, assim como o estado da próxima reunião: número, data, hora, local/plataforma e preparação. Os campos não confirmados ficam explicitamente assinalados.

## Atualizar o PDF a partir do resumo

```bash
/usr/bin/python3 meetings/gpt/gerar_pdf_reuniao.py \
  'meetings/2a_Reuniao 29-10-26/resumo_2a_reuniao_2026-10-29.md' \
  'meetings/2a_Reuniao 29-10-26/resumo_2a_reuniao_2026-10-29.pdf'
```

O gerador usa Cairo e Pango, disponíveis neste ambiente. Nas próximas reuniões, adaptar o número e a data dos dois caminhos.
