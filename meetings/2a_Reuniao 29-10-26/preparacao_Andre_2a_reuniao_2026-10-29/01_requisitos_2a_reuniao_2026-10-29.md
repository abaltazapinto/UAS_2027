# UAS 2027 — 2.ª reunião — 29/10/2026 — Requisitos para André

**Trabalho efetuado:** leitura dirigida do regulamento oficial atualmente ligado em [aerocup.pt](https://aerocup.pt/) e do Handbook. Regulamento **V1.0, 17/09/2026, 34 páginas**. A matriz tem **25 entradas preenchidas**, com origem, cláusula, página, aplicabilidade, responsável proposto e método de verificação.

**Entregável:** [matriz de requisitos em CSV](requisitos_2a_reuniao_2026-10-29.csv). **Fontes e calendário:** [registo de fontes](fontes_regulamento_2a_reuniao_2026-10-29.md).

## Como utilizar a matriz

A referência “p.” é a numeração impressa; “PDF” é a posição da página no ficheiro, começando em 1. As responsabilidades e os métodos de verificação são propostas de organização deste trabalho. Todos os estados começam em **Não validado**: investigar um requisito não demonstra que a aeronave o cumpre.

| Prioridade | Entradas | Trabalho já preparado para a próxima reunião |
|---|---|---|
| Decisão de âmbito | REG-01, REG-02 | Separar a classe pretendida, o responsável global da equipa e a liderança conjunta do departamento. A Manual Class permite o percurso inicial sem autonomia obrigatória. |
| Escolha técnica | REG-03 a REG-06 | Base para comparar autopilotos, identificar autorizações necessárias e planear a recuperação de controlo. |
| Comunicações | REG-07 a REG-10 | Critérios para avaliar RC e elaborar os casos de perda de sinal; requisitos RC e telemetria são tratados separadamente. |
| Interfaces com Hardware | REG-11 a REG-17 | Pontos para fechar alimentação, corte externo, conectores, instalação da caixa da organização e cablagem. |
| Evidência de ensaio | REG-18 a REG-22 | Casos de inspeção identificados, com participantes propostos. Execução e conformidade permanecem pendentes. |
| Documentação | REG-23 a REG-25 | Rastreabilidade entre componentes, versão técnica e entregas; registo das correções formais. |

## Matriz de consulta

Todos os estados são **Não validado**. A coluna «origem» do CSV identifica a natureza de cada entrada; REG-03 é recomendação e REG-05 é orientação condicionada a um pedido. A recuperação de controlo e as inspeções do autopiloto dependem dos sistemas implementados. Aplicabilidade, responsáveis e métodos completos estão no CSV.

| ID | Requisito resumido | Cláusula e página |
|---|---|---|
| REG-01 | Confirmar classe: Manual e/ou Automatic | §2.2.1–3; p.2 (PDF 7/34) |
| REG-02 | Identificar Team Leader perante a organização | §2.4.1.4; p.3 (PDF 8/34) |
| REG-03 | Autopilotos COTS ArduPilot/PX4 recomendados | §3.4.1; p.9 (PDF 14/34) |
| REG-04 | Obter autorização para alternativas/modificações de autopiloto | §3.4.1–2; p.9 (PDF 14/34) |
| REG-05 | Preparar código do autopiloto para eventual pedido | §3.4.3; p.9 (PDF 14/34) |
| REG-06 | Permitir recuperação do controlo pelo piloto | §3.4.4; p.9 (PDF 14/34) |
| REG-07 | Rádio RC em 2,4 GHz | §3.5.1.1; p.9 (PDF 14/34) |
| REG-08 | Alcance mínimo RC de 1000 m | §3.5.1.1; p.9 (PDF 14/34) |
| REG-09 | Terminação imediata de voo: fail-safe sempre disponível | §3.5.1.3; p.9 (PDF 14/34) |
| REG-10 | Ação fail-safe até 3 s após perda RC | §3.5.1.4–5; p.10 (PDF 15/34) |
| REG-11 | Bateria separada para eletrónica/comunicações | §3.2.1.4; p.8 (PDF 13/34) |
| REG-12 | Propulsão: máximo 53,4 V; até 12 células em série | §3.2.1.3; p.8 (PDF 13/34) |
| REG-13 | Interruptor externo acessível corta alimentação dos motores | §3.2.2.1; p.8 (PDF 13/34) |
| REG-14 | Acomodar caixa de medição com céu desobstruído | §3.6.1,3; p.10 (PDF 15/34) |
| REG-15 | Integrar caixa na ligação de propulsão por XT90 | §3.6.4; p.10 (PDF 15/34) |
| REG-16 | Usar fixações da caixa e demonstrar integração | §3.6.6; p.10 e fig.3.2 p.11 (PDF 15–16/34) |
| REG-17 | Cabos isolados; conectores críticos firmes; baterias separadas | §4.4.1(a–c); p.14 (PDF 19/34) |
| REG-18 | Ensaiar superfícies e comunicações até 200 m | §4.5.1–3; p.15 (PDF 20/34) |
| REG-19 | Inspeção: potência máxima 30 s e fail-safe | §4.6.1–2; p.15 (PDF 20/34) |
| REG-20 | Demonstrar resposta do autopiloto à inclinação | §4.7.1.1; p.15 (PDF 20/34) |
| REG-21 | Demonstrar safety switch em modo autónomo | §4.7.2.1; p.15 (PDF 20/34) |
| REG-22 | Passar inspeções antes das provas dinâmicas | §4.1.1–2; p.12 (PDF 17/34) |
| REG-23 | Cumprir entregas e prazos do Handbook | §2.7.1.1; p.6 (PDF 11/34); Handbook §2.5 |
| REG-24 | Corrigir documentos em 168 h após pedido | §2.7.2.4–6; p.6 (PDF 11/34) |
| REG-25 | Listar componentes presentes e necessários à operação | §4.2.1,4; p.13 (PDF 18/34) |

As entradas sintetizam as cláusulas identificadas; o texto oficial define as condições completas. O método de verificação proposto em cada linha da folha de cálculo orienta a preparação da evidência.

## Questões que André deve fechar com a equipa

1. **Qual é a classe de inscrição neste ciclo?** A prioridade manual acordada na reunião não substitui a decisão formal MC/AC. O regulamento admite MC e AC com a mesma aeronave (§2.2); autonomia não é imposta à MC.
2. **Quem é o Team Leader global?** A exigência administrativa do regulamento é diferente da liderança partilhada André/Rita e Eduardo/Beatriz.
3. **Que autopiloto e arquitetura se vão estudar primeiro?** ArduPilot e PX4 são recomendações oficiais, sem escolha da equipa até agora. Sistemas alternativos ou modificações podem precisar de autorização.
4. **Qual será o comportamento de perda RC e o mecanismo de recuperação?** Definir critérios verificáveis antes de parametrizar. A matriz aponta a cláusula completa; um retorno genérico à origem não demonstra, por si, cumprimento.
5. **Que dados são necessários de Hardware/Estruturas?** Alimentação, conectores, portas, massas, localização das antenas/sensores e integração da caixa da organização.

## Separação entre decisões e evidência

- **Confirmado na reunião:** André e Rita lideram Software/Comunicações; Eduardo e Beatriz lideram Hardware; começar por voo manual.
- **Preparado neste trabalho:** pesquisa regulamentar, matriz inicial e propostas de verificação/responsabilidade.
- **A decidir em equipa:** classe, arquitetura, componentes e sequência dos ensaios.
- **A demonstrar posteriormente:** comportamento do sistema e aprovação nas inspeções.

**Estado de execução:** leitura e levantamento concluídos. Revisão pela equipa e validação da aeronave pendentes.

