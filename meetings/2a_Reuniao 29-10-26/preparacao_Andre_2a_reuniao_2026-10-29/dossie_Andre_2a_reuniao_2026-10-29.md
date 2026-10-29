# UAS 2027 — 2.ª reunião — 29/10/2026 — Dossiê de André

Preparação de Software/Comunicações: pesquisa realizada, propostas para decisão, interfaces e seguimento.

**Estado:** preparação documental concluída; decisões da equipa e evidências de ensaio mantêm estados próprios. As fontes estão ligadas nos respetivos capítulos.

## Parte 1 — Começar aqui


**O trabalho de preparação está reunido neste pacote:** leitura e síntese do regulamento, matriz de requisitos, pesquisa de plataformas e controladores, proposta de arquitetura, 14 interfaces, sete entidades com contactos verificados, plano de execução e mensagens prontas.

O teu papel confirmado é liderar **Software/Comunicações com Rita**. Hardware fica com **Eduardo e Beatriz**. A primeira prioridade mantém-se no voo manual, com uma base que permita estudar a autonomia. A confirmação das lideranças está em 32:11–32:33 da gravação da 2.ª reunião.

### O que levas para a próxima conversa

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

### As tuas primeiras ações

1. **Alinhar com Rita.** Usar o texto preparado e acordar a divisão inicial. Já existem requisitos, interfaces e pesquisa para apresentar.
2. **Obter as respostas da coordenação.** Membros após votação, acessos, classe/configuração, material existente e representante global da equipa perante a AeroCup.
3. **Dar a tua disponibilidade.** O próximo encontro será por departamento, idealmente na semana de 02/11/2026; dia, hora e plataforma continuam por confirmar.
4. **Rever interfaces com Hardware.** Entregar a matriz a Eduardo e Beatriz e fechar as pendências de maior impacto.
5. **Escolher o primeiro ensaio com a equipa.** O roteiro e os critérios estão preparados; a execução em simulação e a validação do equipamento serão registadas quando acontecerem.

Estas ações dependem de respostas ou decisões pessoais e da equipa. A pesquisa e os documentos que as suportam já estão adiantados.

### Documentos e folhas de trabalho

- [Requisitos e regras](01_requisitos_2a_reuniao_2026-10-29.md) · [matriz CSV](requisitos_2a_reuniao_2026-10-29.csv).
- [Arquitetura e pesquisa técnica](02_arquitetura_pesquisa_2a_reuniao_2026-10-29.md) · [interfaces CSV](interfaces_2a_reuniao_2026-10-29.csv) · [diagrama SVG](arquitetura_2a_reuniao_2026-10-29.svg).
- [Empresas e contactos](03_empresas_contactos_2a_reuniao_2026-10-29.md) · [contactos CSV](empresas_2a_reuniao_2026-10-29.csv).
- [Plano de execução](04_execucao_Andre_2a_reuniao_2026-10-29.md) · [tarefas CSV](tarefas_2a_reuniao_2026-10-29.csv) · [decisões e propostas CSV](decisoes_2a_reuniao_2026-10-29.csv).
- [Mensagens e pauta](05_mensagens_pauta_2a_reuniao_2026-10-29.md).
- [Índice das fontes da pesquisa](fontes_pesquisa_2a_reuniao_2026-10-29.md).
- [Briefing em PDF](briefing_Andre_2a_reuniao_2026-10-29.pdf) · [dossiê completo em PDF](dossie_Andre_2a_reuniao_2026-10-29.pdf).

Os CSV usam UTF-8 e vírgula como separador; selecionar essas opções se a folha de cálculo pedir o formato de importação. As fontes oficiais estão junto das afirmações nos documentos de pesquisa. As versões e páginas do regulamento constam do registo de fontes.

Para atualizar os dois PDFs após editar os documentos, executar `python3 montar_dossie_2a_reuniao_2026-10-29.py` nesta pasta.

### Como apresentar o estado do trabalho

Podes dizer: **«Já tenho uma primeira base de requisitos, arquitetura, interfaces e pesquisa de soluções. Quero revê-la convosco para fecharmos as primeiras decisões e distribuirmos as tarefas.»**

A preparação documental está feita. As mensagens são rascunhos locais; os contactos permanecem por realizar; a aceitação da equipa e os ensaios ficam identificados como pendentes. A conformidade de um sistema só poderá ser marcada depois de existir evidência do requisito no sistema efetivamente escolhido.

**Primeiro resultado a propor ao departamento:** aprovar uma baseline 0.1 de requisitos/interfaces e escolher o primeiro ensaio em simulação, com responsáveis e prazo combinados.

---

## Parte 2 — Requisitos e regulamento


**Trabalho efetuado:** leitura dirigida do regulamento oficial atualmente ligado em [aerocup.pt](https://aerocup.pt/) e do Handbook. Regulamento **V1.0, 17/09/2026, 34 páginas**. A matriz tem **25 entradas preenchidas**, com origem, cláusula, página, aplicabilidade, responsável proposto e método de verificação.

**Entregável:** [matriz de requisitos em CSV](requisitos_2a_reuniao_2026-10-29.csv). **Fontes e calendário:** [registo de fontes](fontes_regulamento_2a_reuniao_2026-10-29.md).

### Como utilizar a matriz

A referência “p.” é a numeração impressa; “PDF” é a posição da página no ficheiro, começando em 1. As responsabilidades e os métodos de verificação são propostas de organização deste trabalho. Todos os estados começam em **Não validado**: investigar um requisito não demonstra que a aeronave o cumpre.

| Prioridade | Entradas | Trabalho já preparado para a próxima reunião |
|---|---|---|
| Decisão de âmbito | REG-01, REG-02 | Separar a classe pretendida, o responsável global da equipa e a liderança conjunta do departamento. A Manual Class permite o percurso inicial sem autonomia obrigatória. |
| Escolha técnica | REG-03 a REG-06 | Base para comparar autopilotos, identificar autorizações necessárias e planear a recuperação de controlo. |
| Comunicações | REG-07 a REG-10 | Critérios para avaliar RC e elaborar os casos de perda de sinal; requisitos RC e telemetria são tratados separadamente. |
| Interfaces com Hardware | REG-11 a REG-17 | Pontos para fechar alimentação, corte externo, conectores, instalação da caixa da organização e cablagem. |
| Evidência de ensaio | REG-18 a REG-22 | Casos de inspeção identificados, com participantes propostos. Execução e conformidade permanecem pendentes. |
| Documentação | REG-23 a REG-25 | Rastreabilidade entre componentes, versão técnica e entregas; registo das correções formais. |

### Matriz de consulta

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

### Questões que André deve fechar com a equipa

1. **Qual é a classe de inscrição neste ciclo?** A prioridade manual acordada na reunião não substitui a decisão formal MC/AC. O regulamento admite MC e AC com a mesma aeronave (§2.2); autonomia não é imposta à MC.
2. **Quem é o Team Leader global?** A exigência administrativa do regulamento é diferente da liderança partilhada André/Rita e Eduardo/Beatriz.
3. **Que autopiloto e arquitetura se vão estudar primeiro?** ArduPilot e PX4 são recomendações oficiais, sem escolha da equipa até agora. Sistemas alternativos ou modificações podem precisar de autorização.
4. **Qual será o comportamento de perda RC e o mecanismo de recuperação?** Definir critérios verificáveis antes de parametrizar. A matriz aponta a cláusula completa; um retorno genérico à origem não demonstra, por si, cumprimento.
5. **Que dados são necessários de Hardware/Estruturas?** Alimentação, conectores, portas, massas, localização das antenas/sensores e integração da caixa da organização.

### Separação entre decisões e evidência

- **Confirmado na reunião:** André e Rita lideram Software/Comunicações; Eduardo e Beatriz lideram Hardware; começar por voo manual.
- **Preparado neste trabalho:** pesquisa regulamentar, matriz inicial e propostas de verificação/responsabilidade.
- **A decidir em equipa:** classe, arquitetura, componentes e sequência dos ensaios.
- **A demonstrar posteriormente:** comportamento do sistema e aprovação nas inspeções.

**Estado de execução:** leitura e levantamento concluídos. Revisão pela equipa e validação da aeronave pendentes.


---

## Parte 3 — Arquitetura e pesquisa técnica


**Preparado para André e Rita. Estado: proposta técnica para discutir com a equipa. Pesquisa documental realizada em 29/10/2026; seleção de equipamentos e ensaios ainda por executar.**

### 1. Proposta pronta para apresentar

Proponho usar **ArduPilot Plane como primeira opção de estudo e simulação**, mantendo **PX4 como alternativa comparada**. A primeira arquitetura deve aproveitar um controlador de voo existente, com controlo RC, telemetria, sensores e registo de dados. O desenvolvimento segue uma sequência de validação manual, assistida e autónoma, mantendo uma base comum entre as fases.

Esta recomendação é uma análise técnica preparada após a reunião. A equipa ainda precisa de confirmar **configuração da aeronave, classe de competição, inventário, orçamento e requisitos**. Asa fixa convencional e híbrido/VTOL continuam como possibilidades; a referência a um avião convencional neste documento é um cenário de estudo, não uma configuração aprovada.

**Entregável inicial proposto:** arquitetura de ligações, matriz de interfaces e demonstração em simulação de comunicação com a estação de terra, antes de selecionar todos os componentes físicos. A matriz já está preenchida em [interfaces_2a_reuniao_2026-10-29.csv](interfaces_2a_reuniao_2026-10-29.csv).

### 2. ArduPilot Plane e PX4 — comparação aplicada

| Critério | ArduPilot Plane | PX4 |
|---|---|---|
| Tipos de aeronave | Documentação inclui avião convencional, asa voadora e QuadPlane VTOL. | Documentação separa aviões de asa fixa e várias configurações VTOL. |
| Evolução do controlo | Inclui modos manuais e autónomos na mesma plataforma. | Inclui modos Manual, Stabilized e Mission para asa fixa. |
| Ferramentas de terra | Mission Planner, MAVProxy e outras estações compatíveis; QGroundControl também suporta ArduPilot. | QGroundControl é a ferramenta natural para configuração e acompanhamento. |
| Primeiro ensaio no Linux de André | SITL com `sim_vehicle.py` e MAVProxy; QGroundControl pode acompanhar por MAVLink. | Caminho documentado de simulação e configuração com QGroundControl; requer preparar o ambiente correspondente. |
| Razão para estudar primeiro | Encaixa na progressão pretendida e oferece um percurso direto de SITL para Plane. | Alternativa adequada se a equipa já tiver experiência, equipamento ou um fluxo PX4 estabelecido. |
| Decisão que falta | Validar com Rita, Hardware e coordenação; inventariar primeiro o material disponível. | A mesma validação; evitar desenvolver em duas plataformas simultaneamente sem necessidade. |

A comparação de adequação é uma avaliação deste documento; as capacidades vêm das [introdução oficial ao Plane](https://ardupilot.org/plane/docs/introduction.html), [documentação PX4 de asa fixa v1.17](https://docs.px4.io/v1.17/en/frames_plane/) e [QGroundControl](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/).

#### Versões para tornar o primeiro ensaio reproduzível

- **ArduPlane:** o diretório oficial `stable/Pixhawk6C` identifica **V4.7.2**, commit **fb773567896014da007bca58358704d4a0d8516f**, com data de 11/10/2026. O diretório de Pixhawk6X identifica a mesma versão. É a referência documental encontrada, não uma instalação feita neste projeto. [Metadata 6C](https://firmware.ardupilot.org/Plane/stable/Pixhawk6C/git-version.txt), [metadata 6X](https://firmware.ardupilot.org/Plane/stable/Pixhawk6X/git-version.txt).
- **PX4:** a documentação consultada apresenta **v1.17** como estável. Fixar também o patch/tag e o commit do binário usado se esta alternativa for escolhida. [Guia v1.17](https://docs.px4.io/v1.17/en/frames_plane/).
- **QGroundControl:** usar a documentação de **Stable V5.1**; registar a versão completa instalada e o sistema operativo no primeiro ensaio. [Guia estável](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/).
- **MAVLink:** propor MAVLink 2 quando os dois extremos o suportarem; fixar versão/dialeto da biblioteca na implementação. A versão do protocolo não é a versão do firmware. [MAVLink 2](https://mavlink.io/en/guide/mavlink_2.html).

As páginas `main`/`master` evoluem. O registo de cada ensaio deve guardar versão, commit, parâmetros, cenário e resultado para poder ser repetido.

### 3. Estação de terra: proposta para o ambiente de André

| Ferramenta | Uso preparado | Condição prática |
|---|---|---|
| QGroundControl | Visualização de estado, planeamento, parâmetros, logs e inspeção MAVLink. | Suporta ArduPilot e PX4 e funciona em Linux, Windows e macOS, entre outras plataformas. Usar como candidata para André em Linux. |
| Mission Planner | Configuração, análise e ferramentas do ecossistema ArduPilot. | A documentação de apresentação identifica compatibilidade com Windows. Usar num computador Windows da equipa se se escolher este fluxo. |
| MAVProxy | Interface de desenvolvimento para o primeiro SITL ArduPilot. | É iniciado pelo `sim_vehicle.py` no fluxo documentado; permite separar o ensaio técnico da interface gráfica escolhida para operação. |

Fontes: [QGroundControl estável](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/), [Mission Planner Overview](https://ardupilot.org/planner/docs/mission-planner-overview.html), [Using SITL](https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html).

**Decisão proposta:** um fluxo principal ArduPlane + MAVProxy para o primeiro ensaio de desenvolvimento; QGroundControl como interface gráfica candidata em Linux. Confirmar depois as funções de configuração que a equipa pretende usar e o computador destinado à estação de terra.

### 4. Dois controladores concretos para comparar com Hardware

| Candidato | Factos verificados | Implicação para a escolha |
|---|---|---|
| Holybro Pixhawk 6C | STM32H743; duas IMUs na especificação; 16 saídas PWM; 3 portas série de uso geral, 2 portas GPS e 2 barramentos CAN. O fabricante documenta suporte ArduPilot e PX4. | Primeiro candidato para levantar inventário/cotação. Verificar número de atuadores, portas ocupadas, alimentação, caixa e cabos da variante fornecida. |
| Holybro Pixhawk 6X | STM32H753; arquitetura modular com módulo e base; 3 IMUs e 2 barómetros; 16 PWM, 4 portas série de uso geral, 2 GPS, 2 CAN e Ethernet. O fabricante documenta ambos os firmwares. | Alternativa se a integração justificar modularidade, sensores adicionais ou mais interfaces. Especificar a base e a revisão exatas na cotação. |

Fontes: especificações [6C](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification) e [6X](https://docs.holybro.com/autopilot/pixhawk-6x/technical-specification); firmware [6C](https://docs.holybro.com/autopilot/pixhawk-6c/supported-firmware) e [6X](https://docs.holybro.com/autopilot/pixhawk-6x/supported-firmware).

**Ponto de integração importante:** a especificação do 6C identifica entradas de potência analógicas; a do 6X identifica entradas com SMBus. O conjunto controlador + módulo de potência + cablagem tem de ser selecionado em conjunto. As 16 saídas anunciadas também precisam de um mapa de funções/timers compatível com o firmware e os atuadores escolhidos.

Na documentação do 6X há diferenças de suporte entre revisões: Rev8 e Rev3/4 têm mínimos de firmware diferentes; é ainda assinalada uma incompatibilidade de Rev3/4 com ArduPilot 4.5.3. Verificar a revisão do equipamento efetivamente disponibilizado antes de o programar. [Compatibilidade por revisão](https://docs.holybro.com/autopilot/pixhawk-6x/supported-firmware).

**Critério de fecho:** aproveitar equipamento já existente se satisfizer os requisitos; comparar depois portas, atuadores, massa/dimensão, alimentação, suporte da revisão, disponibilidade e custo do conjunto. Os factos acima não estabelecem um vencedor sem esses dados. Não foi efetuada compra nem assumido preço.

### 5. Arquitetura inicial de ligações

Esquema conceptual proposto para um cenário de asa fixa. As linhas representam funções; o esquema elétrico final depende dos componentes e da matriz de requisitos.

```text
Piloto / emissor RC -- ligação rádio --> recetor RC -- SBUS ou CRSF --> controlador de voo

Computador com GCS <-- ligação de telemetria --> rádio embarcado <-- UART/MAVLink --> controlador

GNSS / bússola ---------------- UART + I2C ou DroneCAN ----------------> controlador
Sensor de velocidade do ar --- I2C ou DroneCAN, conforme modelo ------> controlador
Controlador ------------------ sinais de comando --------------------> servos / ESC
ESC -------------------------- potência ------------------------------> motor

Alimentação de eletrónica ---- regulação e medição -------------------> controlador / recetor / rádio
Alimentação dos servos ------- regulação dimensionada ----------------> servos
Alimentação de propulsão ----- circuito de potência ------------------> ESC

Controlador ------------------ registo local -------------------------> cartão de memória / logs
```

Os barramentos e os sensores são candidatos de integração. A documentação PX4 de [montagem de asa fixa](https://docs.px4.io/main/en/assembly/assembly_fw) descreve controlador, GNSS, bússola, velocidade do ar, RC/telemetria, atuadores e alimentação. Recomenda sensor de velocidade do ar para asa fixa/VTOL; a inclusão concreta deve ser decidida com os requisitos e o desenho da aeronave.

#### RC, telemetria e comunicações internas

- **RC:** transporta os comandos do piloto. SBUS e CRSF são alternativas da ligação recetor–controlador, não nomes da frequência usada pelo rádio. CRSF exige uma porta série adequada; confirmar pinagem, sinal e requisitos do recetor escolhido. [Sistemas RC ArduPilot](https://ardupilot.org/plane/docs/common-rc-systems.html).
- **Telemetria:** transporta estado, parâmetros e mensagens de missão/comando entre controlador e estação de terra. MAVLink é um protocolo candidato; UART é uma interface local, enquanto o rádio constitui o transporte sem fios. Alguns sistemas RC também transportam telemetria. [Telemetria ArduPilot](https://ardupilot.org/plane/docs/common-telemetry-landingpage.html).
- **Comunicações internas:** UART, I2C e CAN/DroneCAN dependem do periférico. A opção tem de caber no mapa de portas e no esquema elétrico. As características das portas do controlador escolhido prevalecem sobre um esquema genérico.

Proponho começar com controlo RC e telemetria tratados como funções distintas, para testar a perda de cada ligação separadamente. Frequência, potência, alcance, antenas e comportamento de falha ficam sujeitos às regras e à revisão da equipa.

Um `HEARTBEAT` MAVLink ajuda a identificar sistemas e a detetar ausência de mensagens esperadas; não demonstra por si só que todos os sensores ou o controlo de voo estejam saudáveis. O protocolo não fixa um prazo universal de perda de ligação: esse prazo terá de vir do requisito e da configuração. [Protocolo heartbeat](https://mavlink.io/en/services/heartbeat.html).

### 6. Divisão de trabalho a propor entre os responsáveis

| Área | Proposta para Software/Comunicações | Articulação necessária |
|---|---|---|
| Firmware e configuração | André e Rita escolhem o fluxo a avaliar, registam parâmetros e evidências. | Hardware confirma suporte e revisão da placa. |
| RC e telemetria | Software define mensagens, modos e comportamentos; identifica interfaces necessárias. | Hardware confirma alimentação, rádio, cabos e ligação física; piloto valida os comandos. |
| Sensores | Software define dados necessários e drivers/configuração a estudar. | Hardware seleciona a alimentação e a compatibilidade elétrica; Estruturas define implantação. |
| Atuadores | Software define funções/canais e valida o mapeamento em conjunto. | Hardware dimensiona servos/ESC e a alimentação; Mecânica confirma sentido e curso úteis. |
| Registo e testes | Software organiza cenários, logs, critérios e rastreabilidade. | Cada departamento valida os resultados relacionados com o seu subsistema. |

São propostas de divisão operacional; só as lideranças conjuntas ficaram atribuídas na 2.ª reunião. André não fica unilateralmente responsável por toda a eletrónica nem são atribuídas tarefas à Rita sem alinhamento com ela.

### 7. Progressão de validação proposta

1. **Simulação:** confirmar configuração, telemetria, mudanças de modo e cenários de perda de ligação com um modelo de teste.
2. **Bancada:** confrontar as interfaces com o equipamento real, verificar alimentação, leitura de sensores, canais e registos; ensaios de atuadores sem hélice e com movimentos controlados.
3. **Controlo manual:** validar a aeronave e o comando pelo piloto segundo o plano de ensaios da equipa.
4. **Assistência:** introduzir estabilização e outras funções apenas depois de validar configuração, sensores e transições.
5. **Autonomia:** executar as funcionalidades exigidas pela classe escolhida, com recuperação de controlo, limites e mecanismos de falha previamente definidos.

A passagem entre fases depende da revisão e dos resultados. Um ensaio SITL não demonstra compatibilidade elétrica, qualidade da ligação rádio ou aptidão para voo da aeronave real.

### 8. Primeiro ensaio SITL — guião pronto, ainda não executado

**Estado atual: não instalado/não executado neste trabalho.** Este guião usa o fluxo oficial ArduPilot; pressupõe um clone preparado e dependências disponíveis. A referência de versão a reproduzir é a indicada na secção 2, com o commit efetivamente utilizado registado no resultado.

Depois de preparado esse ambiente, no diretório do clone ArduPilot:

```bash
./Tools/autotest/sim_vehicle.py -v ArduPlane -f plane --console --map
```

O comando lança o modelo `plane` de estudo e MAVProxy. O modelo deverá ser alterado se a equipa aprovar outra configuração. O manual [Using SITL](https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html) descreve este fluxo e as opções para ligar outra GCS; o [guia Linux](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html) trata da preparação do ambiente. O modelo `plane` não é uma aprovação de asa fixa para o projeto.

#### Critérios propostos e evidências a guardar

| Ensaio | Critério de aceitação proposto | Estado |
|---|---|---|
| S01 — arranque e identificação | Guardar versão/commit, modelo, parâmetros iniciais e identificação MAVLink do veículo. | Não executado. |
| S02 — dados na GCS | Obter estado, modo, atitude e dados de navegação simulados e guardar um log legível. | Não executado. |
| S03 — entrada manual e mudança de modo | Registar os comandos e confirmar a resposta prevista no modelo; documentar transições e recuperação manual. | Não executado. |
| S04 — perda de telemetria/GCS | Confirmar a reação configurada para perda da GCS e o seu registo, separadamente da perda RC. | Não executado; política a aprovar. |
| S05 — perda RC | Confirmar deteção, ação e tempo segundo o requisito regulamentar aplicável e a configuração aprovada. | Não executado; requisito/configuração a ligar à matriz. |
| S06 — dados degradados | Simular os cenários de sensor/alimentação suportados pelo ambiente e verificar os avisos e ações definidos. | Não executado; cenários a fechar. |
| B01 — mapa elétrico | Validar pinagem, tensões de operação, massas, conectores e alimentação contra a revisão real antes das ligações. | Não executado; equipamento por selecionar. |
| B02 — saídas e sensores reais | Confirmar canais, sentido e limites de atuação, leitura dos sensores e gravação de logs no conjunto de bancada. | Não executado. |

As reações de perda RC, GCS e bateria são configuráveis no Plane e têm de ser coerentes com os requisitos, não copiadas de um valor de exemplo. A [documentação de failsafe Plane](https://ardupilot.org/plane/docs/apms-failsafe-function.html) distingue estes casos. Guardar o ficheiro de parâmetros, o log, as condições de ensaio e a comparação entre resultado esperado e observado em cada execução.

### 9. Decisões a fechar no próximo encontro

- Qual é a classe de competição e que configuração de aeronave está efetivamente em avaliação?
- Que controlador, rádio, sensores e computador existem já na equipa?
- Aceitamos ArduPlane como primeira opção para simulação, mantendo PX4 como alternativa documentada?
- Quem prepara o primeiro SITL e quem revê a matriz de interfaces com Hardware?
- Que dados, comportamento de falha e evidências são indispensáveis para o primeiro entregável?
- Como dividimos o trabalho entre André, Rita e os restantes elementos sem duplicar configurações?

**Resultado da pesquisa:** duas plataformas comparadas, duas placas concretas verificadas, arquitetura proposta, 14 interfaces preenchidas e critérios de ensaio preparados. A escolha da equipa e as evidências de execução continuam abertas.

### 10. Referências de outras equipas

Não consegui confirmar uma lista de componentes de uma equipa portuguesa da AeroCup nas fontes públicas consultadas. Os dois exemplos seguintes têm evidência primária; pertencem a contextos com missões e regulamentos diferentes dos da AeroCup.

**Beihang Aeromodelling Team — UAS Challenge 2026.** A universidade informa que a equipa integrou **ArduPilot num modelo de voo em X-Plane**, usando simulação iterativa antes e durante o desenvolvimento. O artigo é de 09/07/2026. Demonstra uma combinação concreta de autopiloto e simulador numa equipa universitária; não identifica uma placa que possamos adotar por comparação direta. [Relato oficial da Beihang University](https://ev.buaa.edu.cn/info/1022/3213.htm).

**CUAir — Cornell University, documentação de 2015–2016.** O repositório da própria equipa documenta utilizações específicas de **ArduPilot** e faz referência à calibração através do **Mission Planner**, com configuração de failsafe associada às suas regras de competição. É uma referência histórica de integração, não uma afirmação sobre o equipamento atual da equipa. A identidade universitária é confirmada no seu site. [Documentação técnica CUAir](https://github.com/CUAir/Autopilot/blob/master/docs/ardupilot.rst), [site da equipa](https://cuair.org/).

**Aplicação proposta ao ISEP:** aproveitar o método — simular, documentar configuração, registar resultados e confrontar falhas com os requisitos — mantendo a escolha da placa, os parâmetros e as regras próprios do nosso projeto. Estes exemplos sustentam o estudo de uma plataforma existente; não provam adequação automática à nossa aeronave.

---

## Parte 4 — Empresas e contactos


**Entregável de André:** pesquisa preenchida de fornecedores e potenciais interlocutores técnicos, pronta a entregar à área de empresas/patrocínios. **Verificação de fontes públicas: 29/10/2026.** A lista inclui sete entidades; o INESC TEC é identificado como parceiro científico potencial, e não como empresa fornecedora.

Esta é uma pesquisa nova. Não representa contactos pessoais de André, parcerias existentes ou disponibilidade das entidades para apoiar o projeto. Todas estão no estado **«não contactada»**. A prioridade abaixo é uma proposta baseada na utilidade para o arranque e na proximidade, sem estimar a probabilidade de patrocínio.

### Lista selecionada

| Prioridade | Entidade e capacidade confirmada | Interesse proposto para UAS 2027 e canal público |
|---|---|---|
| P1 | **botnroll.com / SAR — Guimarães.** Loja de robótica com componentes, sensores, módulos e material de prototipagem. | Identificar material para bancada e pedir condições para uma lista de componentes já definida. Contacto: **botnroll@botnroll.com**. [Catálogo e contactos oficiais](https://www.botnroll.com/pt/contacte-nos). |
| P1 | **INESC TEC / CRAS — Porto, com presença no ISEP.** Centro de investigação em robótica e sistemas autónomos, incluindo perceção, navegação e controlo. | Pedir encaminhamento para uma conversa de orientação sobre arquitetura e validação; a possibilidade de colaboração depende da instituição. Contacto geral: **info@inesctec.pt**. [Atividade do CRAS](https://www.inesctec.pt/pt/centros/cras), [contactos e presença no ISEP](https://www.inesctec.pt/pt/contactos). |
| P1 | **Castro Electrónica — Portugal.** Catálogo com instrumentação, componentes e material de eletrónica; inclui multímetros e osciloscópios. | Avaliar material de bancada ou consumíveis antes de pedir orçamento/apoio para itens concretos. [Formulário oficial](https://www.castroelectronica.pt/ajuda/formulario-contacto); o apoio ao cliente publica **info@castroelectronica.pt**. [Instrumentação](https://www.castroelectronica.pt/en/loja-virtual/osciloscpios-1), [email publicado pelo apoio](https://castroelectronica.freshdesk.com/support/solutions/articles/202000087837-atraso-nas-encomendas). |
| P2 | **Holybro — fornecedor internacional de autopilotos.** Documenta, por exemplo, o controlador Pixhawk 6C e as respetivas interfaces. | Depois da seleção técnica, esclarecer um conjunto controlador/acessórios e eventual apoio ao projeto. Patrocínios devem seguir para a **equipa comercial**, através do [formulário comercial](https://holybro.com/pages/sales-related-inquiry). [Documentação do produto](https://docs.holybro.com/autopilot/pixhawk-6c/overview.md), [orientação oficial sobre patrocínios](https://holybro.com/pages/technical-support). |
| P2 | **CEiiA — Matosinhos.** Centro de engenharia e desenvolvimento de produto com atividade em aeronáutica. | Explorar uma sessão de orientação sobre integração entre eletrónica, estrutura e validação. Contacto geral: **ceiia@ceiia.com**. [Atividade aeronáutica](https://www.ceiia.com/aeronautics), [contactos](https://www.ceiia.com/contacts). |
| P3 | **UAVision — Ventosa, Portugal.** Desenvolve sistemas não tripulados, aviónica, ligações de dados e estações de controlo. | Explorar uma conversa sobre integração e testes de sistemas UAS, com âmbito académico e civil. Contacto geral: **info@uavision.com**. [Capacidades e contactos oficiais](https://www.uavision.com/). |
| P3 | **TEKEVER — contacto em Lisboa.** Trabalha em sistemas aéreos não tripulados, software e autonomia. | Explorar uma sessão sobre desenvolvimento de software, organização de testes e integração de sistemas, com âmbito académico e civil. Contacto geral: **info@tekever.com**. [Atividade](https://www.tekever.com/why-us/), [contactos oficiais](https://www.tekever.com/contact/). |

**P1:** analisar primeiro para necessidades imediatas e encaminhamento local. **P2:** abordar quando a arquitetura ou o pedido estiverem suficientemente definidos. **P3:** explorar mentoria especializada, sem tratar estas entidades como fornecedores obrigatórios do primeiro protótipo.

### Encaminhamento e responsabilidades

A reunião atribuiu os pedidos de patrocínio e a comunicação com empresas à área dedicada, com apoio técnico dos departamentos quando necessário (**28:18–29:16**). A coordenação anunciou um documento partilhado com empresas, contactos e emails (**31:59–33:17**).

Proposta para utilizar esta pesquisa:

1. A área de empresas/patrocínios verifica quais as entidades já abordadas, para evitar duplicação de contactos.
2. André e Rita identificam o pedido técnico de Software/Comunicações; Eduardo e Beatriz complementam os itens de Hardware e bancada.
3. A equipa escolhe as primeiras entidades e o tipo de pedido: esclarecimento técnico, mentoria, orçamento ou eventual apoio em espécie.
4. A área de empresas/patrocínios faz o contacto e atualiza a folha de seguimento. André participa no esclarecimento técnico quando necessário.

Para fornecedores, o pedido deve acompanhar uma necessidade identificada: item/função, quantidade proposta, interfaces e restrições relevantes. Para mentoria, uma página com o objetivo da equipa e duas ou três dúvidas concretas é um ponto de partida útil. O pedido não deve pressupor componentes já aprovados, orçamento disponível ou contrapartidas comerciais acordadas.

### Informação já preenchida e informação por decidir

- **Concluído:** seleção de sete entidades; identificação de atividade relevante; confirmação dos canais públicos; proposta de prioridade e de pedido inicial; exportação para [CSV](empresas_2a_reuniao_2026-10-29.csv).
- **A decidir pela equipa:** entidades a abordar primeiro, conteúdo final do pedido e responsável nominal pela comunicação.
- **Dependências técnicas:** arquitetura, controlador, material já disponível e lista de necessidades antes de pedir fornecimento de componentes específicos.
- **Seguimento:** estado inicial «não contactada» em todas as linhas; atualizar apenas quando existir uma ação ou resposta real.

O canal público de suporte técnico da Holybro é **support@holybro.com**, mas a própria empresa encaminha patrocínios para a equipa comercial e limita o seu suporte de software. Esse email é registado no CSV com essa distinção; o formulário comercial é o canal proposto para o pedido de apoio. [Fonte oficial](https://holybro.com/pages/technical-support).

---

## Parte 5 — Plano de execução de André


**Papel confirmado:** liderança conjunta de Software/Comunicações com Rita. Hardware é liderado por Eduardo e Beatriz. **Base:** resumo da 2.ª reunião, em especial 32:11–32:33. **Estado deste plano:** proposta de execução preparada após a reunião; os responsáveis e os prazos abaixo precisam de alinhamento com a equipa.

### 1. Trabalho de preparação já executado

| Pedido da reunião | Entregável preparado | O que falta para o fechar com a equipa |
|---|---|---|
| Ler as regras relevantes | Síntese das regras e matriz de requisitos, com secções, fontes e verificação proposta | Confirmar classe e aplicabilidade; rever os requisitos em conjunto. |
| Investigar soluções | Comparação ArduPilot/PX4, estações de controlo e candidatos de hardware | Confirmar configuração, material existente e restrições; escolher a solução. |
| Articular Hardware e Software | Arquitetura funcional e matriz de interfaces preenchida | Fechar sinais, alimentação, conectores, versões e responsabilidades. |
| Reunir empresas e contactos | Sete entidades pesquisadas e folha de contactos | Encaminhar para a área de empresas/patrocínios e escolher os pedidos. |
| Organizar o departamento | Proposta de divisão, tarefas e critérios de conclusão | Rita e restantes membros participam na distribuição final. |
| Preparar o próximo encontro | Pauta de 45 minutos, perguntas e textos de contacto prontos | Confirmar participantes, disponibilidades, dia, hora e plataforma. |

Os documentos estão preparados para discussão. Ensaios, implementação, compras e aceitação da equipa têm estados próprios e permanecem pendentes.

### 2. Ordem de execução a partir daqui

#### P0 — Fechar o contexto com Rita e coordenação

**Proposta para André:** usar os textos do documento de mensagens para alinhar três assuntos: membros do departamento, classe de competição e acessos. A reunião já definiu as lideranças; a conversa seguinte deve avançar para trabalho concreto.

Resultados necessários:

- Saber quem entrou em Software/Comunicações após a votação.
- Ter o acesso ao grupo/Discord e ao local dos documentos.
- Confirmar com a coordenação a classe inscrita ou pretendida e a configuração da aeronave em estudo.
- Confirmar quem é o representante global da equipa perante a AeroCup e quem acompanha inscrição e entregas.
- Saber se existe controlador, rádio, recetor, sensores, computador de bancada ou outro material aproveitável.
- Recolher a disponibilidade real dos membros para a reunião por departamento.

**Critério de conclusão:** estas respostas ficam registadas no documento de decisões e na folha de tarefas. A data da reunião só é fechada depois de cruzar disponibilidades.

#### P1 — Apresentar uma primeira base técnica já preenchida

**Proposta de divisão inicial, a acordar:** André começa pela manutenção dos requisitos, interfaces e documentação de ensaios; Rita escolhe a área que prefere aprofundar, por exemplo comunicações/GCS ou comparação das plataformas. A proposta usa o trabalho de preparação já disponível e permite redistribuição segundo experiência e disponibilidade.

Na primeira conversa de trabalho, apresentar:

1. A matriz de requisitos, com cada regra ligada à respetiva fonte e a um método de verificação.
2. A arquitetura candidata comum ao voo manual e à evolução autónoma.
3. A matriz de interfaces, destacando as respostas necessárias de Hardware.
4. A comparação de plataformas, com uma recomendação de estudo e as alternativas.

**Critério de conclusão:** requisitos aceites ou corrigidos; dúvidas com responsável; decisão de plataforma registada ou uma lista curta de informação que falta para decidir.

#### P2 — Fechar as interfaces com Eduardo e Beatriz

Levar a matriz de interfaces para a conversa de integração. Os pontos de maior impacto são alimentação da eletrónica, ligações entre recetor e controlador, saídas para atuadores, sensores, telemetria e espaço/massa para integração na estrutura.

**Critério de conclusão:** para cada ligação crítica, existe uma função definida, um interlocutor em cada departamento e um registo dos dados elétricos/mecânicos ainda por fechar. A matriz contém as ligações a discutir; os protocolos candidatos precisam de validação.

#### P3 — Fazer a primeira demonstração de software

**Proposta:** começar em simulação/bancada pela comunicação entre controlador simulado e estação de controlo, pela observação dos modos/estado e pela recolha de um registo de ensaio. O documento de arquitetura contém o roteiro e os casos a observar.

A execução depende da plataforma escolhida e do computador disponível. O pacote atual deixa o roteiro preparado; não contém resultados de um simulador ou de hardware que tenha sido ensaiado.

**Evidência a produzir quando o ensaio for executado:** versões utilizadas, configuração, caso executado, resultado esperado e observado, log e conclusão. Uma ligação estabelecida ou um heartbeat observado demonstram conectividade naquele ensaio; os requisitos de controlo e de falha precisam dos seus próprios testes.

#### P4 — Encaminhar a pesquisa de empresas

Entregar a folha preenchida à área de empresas/patrocínios. Essa área confirma contactos anteriores e escolhe a abordagem; André e Rita fornecem o pedido técnico. A lista prepara o trabalho de contacto, sem pressupor interesse ou apoio das entidades.

### 3. Entregável a propor para o primeiro ciclo do departamento

**Proposta:** baseline inicial de Software/Comunicações, versão 0.1, composta por requisitos aplicáveis, diagrama funcional, interfaces críticas e plano de um primeiro ensaio em simulação.

Critérios de aceitação propostos:

- Cada requisito tem origem, aplicabilidade e forma de verificação identificadas.
- As escolhas técnicas aprovadas ficam separadas das opções em avaliação.
- Cada interface crítica tem interlocutores e pendências registadas.
- O primeiro ensaio tem ambiente, resultado esperado e evidência a guardar definidos.
- André e Rita revêm a baseline; Hardware valida as interfaces que lhe dizem respeito.

O prazo deve ser combinado no primeiro encontro. Este documento propõe o conteúdo e os critérios; a reunião de 29/10 não fixou uma data de entrega para esta baseline.

### 4. O que precisas de compreender antes de apresentar o trabalho

Uma revisão de 15–20 minutos pode concentrar-se nestes pontos:

| Conceito | Ideia que deves conseguir explicar |
|---|---|
| Controlador de voo | Recebe comandos e sensores, executa o software de controlo e comanda as saídas. A placa e o firmware têm de ser compatíveis. |
| RC | Ligação de comando do piloto. O protocolo do recetor até à placa é uma interface distinta da ligação rádio pelo ar. |
| Telemetria | Troca de estado/dados/comandos com a estação de controlo; requisitos e falhas devem ser tratados separadamente do comando RC. |
| MAVLink | Protocolo de mensagens usado entre componentes; não escolhe por si só o rádio, a frequência ou a interface elétrica. |
| GCS | Aplicação no computador de terra para configuração, observação e, quando aplicável, missões. |
| SITL | Execução de software de voo num ambiente simulado; permite estudar integração e falhas sem validar a aeronave física. |
| Interface | Contrato entre subsistemas: função, protocolo, níveis elétricos, conector, alimentação, configuração e responsável. |
| Verificação | Evidência de que um requisito foi satisfeito num contexto definido; investigação e seleção de componentes são passos anteriores. |

As fontes técnicas e os limites das opções estão no documento de arquitetura. Os valores normativos estão na matriz de requisitos.

### 5. Riscos de planeamento e resposta proposta

| Tema | Consequência prática | Resposta proposta |
|---|---|---|
| Classe ou configuração ainda em aberto | Requisitos e interfaces podem mudar | Fechar com a coordenação; identificar aplicabilidade condicional na matriz. |
| Material disponível desconhecido | Comparar compras que talvez sejam desnecessárias | Pedir inventário antes da seleção. |
| Interfaces elétricas indefinidas | Incompatibilidades e retrabalho na integração | Rever a matriz com Hardware antes de ligar componentes. |
| Dois departamentos a estudar o mesmo problema | Trabalho duplicado | André/Rita e Eduardo/Beatriz atribuem um responsável por assunto e partilham resultados. |
| Versões não registadas | Ensaios difíceis de repetir | Guardar versões, configuração e logs por ensaio. |
| Disponibilidade ainda não recolhida | Reunião e tarefas sem responsáveis efetivos | Cruzar disponibilidades e atribuir tarefas pequenas com critérios claros. |

### 6. Dependências pessoais e externas

O trabalho de pesquisa e os documentos já estão preparados. As respostas que ainda precisam de vir de pessoas são: a tua disponibilidade, a preferência de Rita na divisão de tarefas, a composição final do grupo, os acessos, o inventário, a classe/configuração e a aceitação das propostas.

A [folha de tarefas](tarefas_2a_reuniao_2026-10-29.csv) distingue preparação concluída, propostas por rever e dependências externas. A pauta e os textos estão no [documento de mensagens e reunião](05_mensagens_pauta_2a_reuniao_2026-10-29.md).

### 7. Pontos administrativos para a coordenação

O Handbook 2027, v1.0, secções 2.4.1 e 3.1, prevê um representante global da equipa e indica o fim das inscrições em **21/01/2027 às 23:59**, com lugares limitados. O fuso desse prazo não está explicitado nessa passagem. A co-liderança de um departamento não identifica, por si, esse representante. André deve obter a confirmação do estado da inscrição e do interlocutor; a administração geral continua com a coordenação. [Handbook oficial](https://firebasestorage.googleapis.com/v0/b/aerocup-website.firebasestorage.app/o/public%2FAeroCup_2027_Handbook_v1_0.pdf?alt=media&token=e7ad08ae-707b-469c-875d-38f947bcdf6e).

O site anuncia 8–12 de julho de 2027; o Handbook inclui 13 de julho como dia de partida. Confirmar mais perto do evento os dias necessários para logística. Esta informação não altera o estado do próximo encontro do departamento, que continua sem dia e hora fixados. [Site oficial](https://aerocup.pt/).

---

## Parte 6 — Mensagens e pauta do próximo encontro


**Estado:** textos preparados em nome de André, para utilização no seguimento da 2.ª reunião. A pauta é uma proposta. A data, a hora e a plataforma do próximo encontro continuam por confirmar. Os textos abaixo estão guardados localmente como rascunhos.

### 1. Mensagem para Rita

Olá Rita! Já preparei uma primeira base para começarmos Software/Comunicações: requisitos da AeroCup, comparação de soluções, proposta de arquitetura e uma lista de interfaces para alinharmos com Hardware.

Proponho usarmos isto no próximo encontro para confirmar os membros do departamento, dividir as primeiras tarefas e escolher um entregável pequeno. Posso começar pela organização dos requisitos, interfaces e registos de ensaio; diz-me que parte preferes aprofundar e ajustamos a divisão juntos.

Também deixei um roteiro para um primeiro ensaio em simulação, depois de escolhermos a plataforma. Ainda temos de cruzar disponibilidades e confirmar os acessos. Estou entusiasmado com os próximos passos!

### 2. Mensagem para a coordenação

Olá! Já organizei uma primeira base de trabalho para Software/Comunicações, com requisitos, pesquisa de soluções, interfaces e uma lista de empresas/contactos para entregar à área de patrocínios.

Para fecharmos a preparação com a Rita, podem partilhar o resultado da distribuição dos membros, os acessos ao grupo/Discord e o local dos documentos? Precisávamos também de confirmar a classe de competição pretendida ou já inscrita, o estado da configuração da aeronave e o material eletrónico que já existe.

Podem também confirmar quem representa a equipa perante a AeroCup e quem acompanha a inscrição e as entregas gerais?

Com os membros definidos, cruzamos as disponibilidades para o primeiro encontro do departamento, idealmente na próxima semana, como foi falado. A pesquisa de empresas fica pronta para a área responsável confirmar contactos anteriores e decidir as abordagens.

### 3. Mensagem para Eduardo e Beatriz

Olá Eduardo e Beatriz! Preparei uma primeira matriz de interfaces entre Hardware e Software/Comunicações para alinharmos o trabalho dos dois departamentos.

Os pontos principais são alimentação da eletrónica, controlador e recetor, saídas para motor/servos, sensores, telemetria e integração na estrutura. Podem partilhar o material já disponível, as opções que estão a estudar e as restrições de espaço, massa e alimentação que já conhecem?

Proponho fazermos uma revisão curta da matriz com a Rita, para atribuir responsáveis e fechar as primeiras interfaces antes de escolhermos os componentes.

### 4. Encaminhamento para empresas/patrocínios

Olá! Já fiz uma pesquisa inicial de sete entidades que podem ser relevantes para componentes, bancada ou orientação técnica. A folha tem as fontes oficiais, os canais públicos de contacto e um pedido inicial proposto para cada uma.

Podem verificar se alguma já foi abordada e dizer quais faz sentido priorizar? Todos os registos estão como «não contactada». Da nossa parte, eu e a Rita ajudamos a concretizar as necessidades de Software/Comunicações, em articulação com Hardware, para o pedido técnico seguir com informação útil.

### 5. Mensagem ao grupo de Software/Comunicações, quando estiver constituído

Olá a todos! Eu e a Rita ficámos com a liderança conjunta de Software/Comunicações. Já temos uma primeira base de requisitos, pesquisa de plataformas e interfaces para discutir convosco.

Para o primeiro encontro, proponho confirmarmos o que cada um prefere trabalhar, fecharmos as dúvidas mais importantes e escolhermos as primeiras tarefas. Partilhem a vossa disponibilidade para conseguirmos marcar a reunião. Podem também indicar em poucas palavras a experiência ou os temas que gostariam de aprofundar: sensores, comunicações, sistemas embebidos, configuração/simulação ou documentação e testes.

### 6. Pauta proposta — 45 minutos

| Tempo | Tema | Resultado pretendido |
|---|---|---|
| 0–5 min | Membros, disponibilidades e experiência | Lista do grupo e organização inicial confirmadas. |
| 5–12 min | Classe, configuração e regras aplicáveis | Dúvidas prioritárias e interlocutor para as resolver. |
| 12–22 min | Arquitetura e comparação de plataformas | Candidato para o primeiro ensaio ou informação necessária para o escolher. |
| 22–32 min | Interfaces com Hardware | Pendências críticas, responsável de cada lado e informação a pedir. |
| 32–40 min | Primeiras tarefas | Cada tarefa tem responsável, critério de conclusão e prazo combinado. |
| 40–45 min | Confirmação de decisões e seguimento | Registo partilhado e método para acompanhar o trabalho. |

### 7. Perguntas prioritárias, com o trabalho já adiantado

1. Qual é a classe pretendida ou já inscrita? A matriz já distingue requisitos condicionais; falta fixar a aplicabilidade.
2. A configuração da aeronave foi entretanto decidida? A arquitetura proposta terá de a refletir.
3. Que controlador, rádio, recetor, sensores e material de bancada já existem? A comparação deve partir desse inventário.
4. Que interfaces precisam de ficar fechadas primeiro para Estruturas e Hardware avançarem?
5. Qual das plataformas candidatas vamos usar no primeiro ensaio e quem configura o ambiente?
6. Quem assume cada tarefa pequena do primeiro ciclo e que evidência vai entregar?

### 8. Registo a preencher com decisões reais

A proposta de decisão inicial é: aprovar uma baseline 0.1 de requisitos/interfaces, escolher o ambiente do primeiro ensaio e distribuir as tarefas do primeiro ciclo. Esta frase só passa a decisão da equipa depois de discutida e aceite.

No final do encontro, registar: data/hora efetivas, presentes, decisões, opções rejeitadas e motivo relevante, tarefas/responsáveis/prazos combinados, pendências e próximo contacto. A numeração e a data do novo registo devem ser as da reunião que efetivamente ocorrer; o material atual continua associado à 2.ª reunião, de 29/10/2026.

---

## Parte 7 — Fontes do regulamento


**Data de consulta:** 29/10/2026. As versões seguintes foram verificadas através dos links atuais da página oficial.

| Fonte | Identificação e uso |
|---|---|
| [Página oficial AeroCup](https://aerocup.pt/) | Liga atualmente Regulations e Handbook para 2027; origem da verificação das versões. |
| [AeroCup 2027 Regulations V1.0](https://firebasestorage.googleapis.com/v0/b/aerocup-website.firebasestorage.app/o/public%2FAeroCup_2027_Regulations_v1_0.pdf?alt=media&token=8632ec5b-91ec-47b5-84f8-b8a0705dd9cf) | Capa de 17/09/2026; 34 páginas. Fonte principal da matriz. Cláusulas citadas com página impressa e posição PDF. |
| [AeroCup 2027 Handbook V1.0](https://firebasestorage.googleapis.com/v0/b/aerocup-website.firebasestorage.app/o/public%2FAeroCup_2027_Handbook_v1_0.pdf?alt=media&token=e7ad08ae-707b-469c-875d-38f947bcdf6e) | Capa de 01/09/2026; 18 páginas. Fonte do calendário administrativo e da organização do evento. |

### Calendário e pontos a confirmar

- **Inscrição:** Handbook §3.1, p.5 (PDF 9/18): 21/01/2027 às 23:59. A equipa deve confirmar a inscrição com a coordenação e guardar o comprovativo.
- **Entregas técnicas:** os requisitos de submissão remetem para o Handbook (§2.7.1 do regulamento). O calendário detalhado e eventuais atualizações devem ser acompanhados pela coordenação; não foram inventadas datas para o primeiro entregável de André.
- **Datas do evento:** a página inicial apresenta 8–12/07/2027; o Handbook §4.1 apresenta 8–13/07/2027, com saída em 13/07 no programa. Registar esta diferença ao organizar deslocações e confirmar com a organização.
- **Próxima reunião do departamento:** continua sem dia/hora fixados; a intenção registada em 29/10 é reunir na semana seguinte, segundo disponibilidades.

### Limites do levantamento

A matriz é inicial e dirigida a Software/Comunicações e às interfaces imediatas. Regras de missões, dimensionamento estrutural e avaliação estática precisam de análise complementar quando a classe e a configuração forem fechadas. Avisos oficiais e alterações posteriores também integram as regras (§2.5.1.5–6 do regulamento).

Os PDFs foram consultados nas fontes oficiais; este pacote guarda a identificação das versões e os respetivos links primários.

**Estado:** fontes consultadas e rastreabilidade preparada; conformidade ainda não validada.


---

## Parte 8 — Índice das fontes externas


Índice das fontes citadas nos documentos e folhas de trabalho. Cada entrada tem uma ligação própria no PDF. As afirmações e os contextos de utilização permanecem nos respetivos capítulos.

- [F01 — aerocup.pt](https://aerocup.pt/)
- [F02 — introdução oficial ao Plane](https://ardupilot.org/plane/docs/introduction.html)
- [F03 — documentação PX4 de asa fixa v1.17](https://docs.px4.io/v1.17/en/frames_plane/)
- [F04 — QGroundControl](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/)
- [F05 — Metadata 6C](https://firmware.ardupilot.org/Plane/stable/Pixhawk6C/git-version.txt)
- [F06 — metadata 6X](https://firmware.ardupilot.org/Plane/stable/Pixhawk6X/git-version.txt)
- [F07 — MAVLink 2](https://mavlink.io/en/guide/mavlink_2.html)
- [F08 — Mission Planner Overview](https://ardupilot.org/planner/docs/mission-planner-overview.html)
- [F09 — Using SITL](https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html)
- [F10 — 6C](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification)
- [F11 — 6X](https://docs.holybro.com/autopilot/pixhawk-6x/technical-specification)
- [F12 — 6C](https://docs.holybro.com/autopilot/pixhawk-6c/supported-firmware)
- [F13 — 6X](https://docs.holybro.com/autopilot/pixhawk-6x/supported-firmware)
- [F14 — montagem de asa fixa](https://docs.px4.io/main/en/assembly/assembly_fw)
- [F15 — Sistemas RC ArduPilot](https://ardupilot.org/plane/docs/common-rc-systems.html)
- [F16 — Telemetria ArduPilot](https://ardupilot.org/plane/docs/common-telemetry-landingpage.html)
- [F17 — Protocolo heartbeat](https://mavlink.io/en/services/heartbeat.html)
- [F18 — guia Linux](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html)
- [F19 — documentação de failsafe Plane](https://ardupilot.org/plane/docs/apms-failsafe-function.html)
- [F20 — Relato oficial da Beihang University](https://ev.buaa.edu.cn/info/1022/3213.htm)
- [F21 — Documentação técnica CUAir](https://github.com/CUAir/Autopilot/blob/master/docs/ardupilot.rst)
- [F22 — site da equipa](https://cuair.org/)
- [F23 — Catálogo e contactos oficiais](https://www.botnroll.com/pt/contacte-nos)
- [F24 — Atividade do CRAS](https://www.inesctec.pt/pt/centros/cras)
- [F25 — contactos e presença no ISEP](https://www.inesctec.pt/pt/contactos)
- [F26 — Formulário oficial](https://www.castroelectronica.pt/ajuda/formulario-contacto)
- [F27 — Instrumentação](https://www.castroelectronica.pt/en/loja-virtual/osciloscpios-1)
- [F28 — email publicado pelo apoio](https://castroelectronica.freshdesk.com/support/solutions/articles/202000087837-atraso-nas-encomendas)
- [F29 — formulário comercial](https://holybro.com/pages/sales-related-inquiry)
- [F30 — Documentação do produto](https://docs.holybro.com/autopilot/pixhawk-6c/overview.md)
- [F31 — orientação oficial sobre patrocínios](https://holybro.com/pages/technical-support)
- [F32 — Atividade aeronáutica](https://www.ceiia.com/aeronautics)
- [F33 — contactos](https://www.ceiia.com/contacts)
- [F34 — Capacidades e contactos oficiais](https://www.uavision.com/)
- [F35 — Atividade](https://www.tekever.com/why-us/)
- [F36 — contactos oficiais](https://www.tekever.com/contact/)
- [F37 — Handbook oficial](https://firebasestorage.googleapis.com/v0/b/aerocup-website.firebasestorage.app/o/public%2FAeroCup_2027_Handbook_v1_0.pdf?alt=media&token=e7ad08ae-707b-469c-875d-38f947bcdf6e)
- [F38 — AeroCup 2027 Regulations V1.0](https://firebasestorage.googleapis.com/v0/b/aerocup-website.firebasestorage.app/o/public%2FAeroCup_2027_Regulations_v1_0.pdf?alt=media&token=8632ec5b-91ec-47b5-84f8-b8a0705dd9cf)
- [F39 — Fonte na folha empresas_2a_reuniao_2026-10-29](https://www.botnroll.com/pt/)
- [F40 — Fonte na folha interfaces_2a_reuniao_2026-10-29](https://ardupilot.org/plane/docs/common-downloading-and-analyzing-data-logs-in-mission-planner.html)
