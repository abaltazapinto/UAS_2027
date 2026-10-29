# UAS 2027 — 2.ª reunião — 29/10/2026 — André: começar aqui

**O trabalho de preparação está reunido neste pacote:** leitura e síntese do regulamento, matriz de requisitos, pesquisa de plataformas e controladores, proposta de arquitetura, 14 interfaces, sete entidades com contactos verificados, plano de execução e mensagens prontas.

O teu papel confirmado é liderar **Software/Comunicações com Rita**. Hardware fica com **Eduardo e Beatriz**. A primeira prioridade mantém-se no voo manual, com uma base que permita estudar a autonomia. A confirmação das lideranças está em 32:11–32:33 da gravação da 2.ª reunião.

## O que levas para a próxima conversa

| Tema | Base já preparada |
|---|---|
| Regras | Requisitos com fonte, aplicabilidade, responsáveis propostos e método de verificação. |
| Tecnologia | ArduPilot Plane e PX4 comparados; estações de controlo e dois controladores concretos estudados. |
| Integração | Diagrama funcional e 14 interfaces com as pendências a fechar com Hardware. |
| Empresas | Sete entidades com contacto público e pedido técnico inicial proposto. |
| Organização | Ordem de execução, tarefas acompanháveis e proposta de baseline 0.1. |
| Comunicação | Cinco textos prontos para Rita, coordenação, Hardware, patrocínios e futuro grupo. |
| Reunião | Pauta de 45 minutos com resultados pretendidos e perguntas prioritárias. |

**Proposta técnica de arranque:** avaliar ArduPilot Plane em simulação, com MAVProxy e uma GCS candidata em Linux; manter PX4 como alternativa documentada. A comparação está feita para apoiar a decisão de André, Rita e equipa. A plataforma ainda não foi selecionada pela equipa nem instalada neste trabalho.

## As tuas primeiras ações

1. **Alinhar com Rita.** Usar o texto preparado e acordar a divisão inicial. Já existem requisitos, interfaces e pesquisa para apresentar.
2. **Obter as respostas da coordenação.** Membros após votação, acessos, classe/configuração, material existente e representante global da equipa perante a AeroCup.
3. **Dar a tua disponibilidade.** O próximo encontro será por departamento, idealmente na semana de 02/11/2026; dia, hora e plataforma continuam por confirmar.
4. **Rever interfaces com Hardware.** Entregar a matriz a Eduardo e Beatriz e fechar as pendências de maior impacto.
5. **Escolher o primeiro ensaio com a equipa.** O roteiro e os critérios estão preparados; a execução em simulação e a validação do equipamento serão registadas quando acontecerem.

Estas ações dependem de respostas ou decisões pessoais e da equipa. A pesquisa e os documentos que as suportam já estão adiantados.

## Documentos e folhas de trabalho

- [Requisitos e regras](01_requisitos_2a_reuniao_2026-10-29.md) · [matriz CSV](requisitos_2a_reuniao_2026-10-29.csv).
- [Arquitetura e pesquisa técnica](02_arquitetura_pesquisa_2a_reuniao_2026-10-29.md) · [interfaces CSV](interfaces_2a_reuniao_2026-10-29.csv) · [diagrama SVG](arquitetura_2a_reuniao_2026-10-29.svg).
- [Empresas e contactos](03_empresas_contactos_2a_reuniao_2026-10-29.md) · [contactos CSV](empresas_2a_reuniao_2026-10-29.csv).
- [Plano de execução](04_execucao_Andre_2a_reuniao_2026-10-29.md) · [tarefas CSV](tarefas_2a_reuniao_2026-10-29.csv) · [decisões e propostas CSV](decisoes_2a_reuniao_2026-10-29.csv).
- [Mensagens e pauta](05_mensagens_pauta_2a_reuniao_2026-10-29.md).
- [Índice das fontes da pesquisa](fontes_pesquisa_2a_reuniao_2026-10-29.md).
- [Briefing em PDF](briefing_Andre_2a_reuniao_2026-10-29.pdf) · [dossiê completo em PDF](dossie_Andre_2a_reuniao_2026-10-29.pdf).

Os CSV usam UTF-8 e vírgula como separador; selecionar essas opções se a folha de cálculo pedir o formato de importação. As fontes oficiais estão junto das afirmações nos documentos de pesquisa. As versões e páginas do regulamento constam do registo de fontes.

Para atualizar os dois PDFs após editar os documentos, executar `python3 montar_dossie_2a_reuniao_2026-10-29.py` nesta pasta.

## Como apresentar o estado do trabalho

Podes dizer: **«Já tenho uma primeira base de requisitos, arquitetura, interfaces e pesquisa de soluções. Quero revê-la convosco para fecharmos as primeiras decisões e distribuirmos as tarefas.»**

A preparação documental está feita. As mensagens são rascunhos locais; os contactos permanecem por realizar; a aceitação da equipa e os ensaios ficam identificados como pendentes. A conformidade de um sistema só poderá ser marcada depois de existir evidência do requisito no sistema efetivamente escolhido.

**Primeiro resultado a propor ao departamento:** aprovar uma baseline 0.1 de requisitos/interfaces e escolher o primeiro ensaio em simulação, com responsáveis e prazo combinados.
