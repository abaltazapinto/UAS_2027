# UAS 2027 — 2.ª reunião — 29/10/2026 — Arquitetura e pesquisa de Software/Comunicações

**Preparado para André e Rita. Estado: proposta técnica para discutir com a equipa. Pesquisa documental realizada em 29/10/2026; seleção de equipamentos e ensaios ainda por executar.**

## 1. Proposta pronta para apresentar

Proponho usar **ArduPilot Plane como primeira opção de estudo e simulação**, mantendo **PX4 como alternativa comparada**. A primeira arquitetura deve aproveitar um controlador de voo existente, com controlo RC, telemetria, sensores e registo de dados. O desenvolvimento segue uma sequência de validação manual, assistida e autónoma, mantendo uma base comum entre as fases.

Esta recomendação é uma análise técnica preparada após a reunião. A equipa ainda precisa de confirmar **configuração da aeronave, classe de competição, inventário, orçamento e requisitos**. Asa fixa convencional e híbrido/VTOL continuam como possibilidades; a referência a um avião convencional neste documento é um cenário de estudo, não uma configuração aprovada.

**Entregável inicial proposto:** arquitetura de ligações, matriz de interfaces e demonstração em simulação de comunicação com a estação de terra, antes de selecionar todos os componentes físicos. A matriz já está preenchida em [interfaces_2a_reuniao_2026-10-29.csv](interfaces_2a_reuniao_2026-10-29.csv).

## 2. ArduPilot Plane e PX4 — comparação aplicada

| Critério | ArduPilot Plane | PX4 |
|---|---|---|
| Tipos de aeronave | Documentação inclui avião convencional, asa voadora e QuadPlane VTOL. | Documentação separa aviões de asa fixa e várias configurações VTOL. |
| Evolução do controlo | Inclui modos manuais e autónomos na mesma plataforma. | Inclui modos Manual, Stabilized e Mission para asa fixa. |
| Ferramentas de terra | Mission Planner, MAVProxy e outras estações compatíveis; QGroundControl também suporta ArduPilot. | QGroundControl é a ferramenta natural para configuração e acompanhamento. |
| Primeiro ensaio no Linux de André | SITL com `sim_vehicle.py` e MAVProxy; QGroundControl pode acompanhar por MAVLink. | Caminho documentado de simulação e configuração com QGroundControl; requer preparar o ambiente correspondente. |
| Razão para estudar primeiro | Encaixa na progressão pretendida e oferece um percurso direto de SITL para Plane. | Alternativa adequada se a equipa já tiver experiência, equipamento ou um fluxo PX4 estabelecido. |
| Decisão que falta | Validar com Rita, Hardware e coordenação; inventariar primeiro o material disponível. | A mesma validação; evitar desenvolver em duas plataformas simultaneamente sem necessidade. |

A comparação de adequação é uma avaliação deste documento; as capacidades vêm das [introdução oficial ao Plane](https://ardupilot.org/plane/docs/introduction.html), [documentação PX4 de asa fixa v1.17](https://docs.px4.io/v1.17/en/frames_plane/) e [QGroundControl](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/).

### Versões para tornar o primeiro ensaio reproduzível

- **ArduPlane:** o diretório oficial `stable/Pixhawk6C` identifica **V4.7.2**, commit **fb773567896014da007bca58358704d4a0d8516f**, com data de 11/10/2026. O diretório de Pixhawk6X identifica a mesma versão. É a referência documental encontrada, não uma instalação feita neste projeto. [Metadata 6C](https://firmware.ardupilot.org/Plane/stable/Pixhawk6C/git-version.txt), [metadata 6X](https://firmware.ardupilot.org/Plane/stable/Pixhawk6X/git-version.txt).
- **PX4:** a documentação consultada apresenta **v1.17** como estável. Fixar também o patch/tag e o commit do binário usado se esta alternativa for escolhida. [Guia v1.17](https://docs.px4.io/v1.17/en/frames_plane/).
- **QGroundControl:** usar a documentação de **Stable V5.1**; registar a versão completa instalada e o sistema operativo no primeiro ensaio. [Guia estável](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/).
- **MAVLink:** propor MAVLink 2 quando os dois extremos o suportarem; fixar versão/dialeto da biblioteca na implementação. A versão do protocolo não é a versão do firmware. [MAVLink 2](https://mavlink.io/en/guide/mavlink_2.html).

As páginas `main`/`master` evoluem. O registo de cada ensaio deve guardar versão, commit, parâmetros, cenário e resultado para poder ser repetido.

## 3. Estação de terra: proposta para o ambiente de André

| Ferramenta | Uso preparado | Condição prática |
|---|---|---|
| QGroundControl | Visualização de estado, planeamento, parâmetros, logs e inspeção MAVLink. | Suporta ArduPilot e PX4 e funciona em Linux, Windows e macOS, entre outras plataformas. Usar como candidata para André em Linux. |
| Mission Planner | Configuração, análise e ferramentas do ecossistema ArduPilot. | A documentação de apresentação identifica compatibilidade com Windows. Usar num computador Windows da equipa se se escolher este fluxo. |
| MAVProxy | Interface de desenvolvimento para o primeiro SITL ArduPilot. | É iniciado pelo `sim_vehicle.py` no fluxo documentado; permite separar o ensaio técnico da interface gráfica escolhida para operação. |

Fontes: [QGroundControl estável](https://docs.qgroundcontrol.com/Stable_V5.1/en/qgc-user-guide/), [Mission Planner Overview](https://ardupilot.org/planner/docs/mission-planner-overview.html), [Using SITL](https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html).

**Decisão proposta:** um fluxo principal ArduPlane + MAVProxy para o primeiro ensaio de desenvolvimento; QGroundControl como interface gráfica candidata em Linux. Confirmar depois as funções de configuração que a equipa pretende usar e o computador destinado à estação de terra.

## 4. Dois controladores concretos para comparar com Hardware

| Candidato | Factos verificados | Implicação para a escolha |
|---|---|---|
| Holybro Pixhawk 6C | STM32H743; duas IMUs na especificação; 16 saídas PWM; 3 portas série de uso geral, 2 portas GPS e 2 barramentos CAN. O fabricante documenta suporte ArduPilot e PX4. | Primeiro candidato para levantar inventário/cotação. Verificar número de atuadores, portas ocupadas, alimentação, caixa e cabos da variante fornecida. |
| Holybro Pixhawk 6X | STM32H753; arquitetura modular com módulo e base; 3 IMUs e 2 barómetros; 16 PWM, 4 portas série de uso geral, 2 GPS, 2 CAN e Ethernet. O fabricante documenta ambos os firmwares. | Alternativa se a integração justificar modularidade, sensores adicionais ou mais interfaces. Especificar a base e a revisão exatas na cotação. |

Fontes: especificações [6C](https://docs.holybro.com/autopilot/pixhawk-6c/technical-specification) e [6X](https://docs.holybro.com/autopilot/pixhawk-6x/technical-specification); firmware [6C](https://docs.holybro.com/autopilot/pixhawk-6c/supported-firmware) e [6X](https://docs.holybro.com/autopilot/pixhawk-6x/supported-firmware).

**Ponto de integração importante:** a especificação do 6C identifica entradas de potência analógicas; a do 6X identifica entradas com SMBus. O conjunto controlador + módulo de potência + cablagem tem de ser selecionado em conjunto. As 16 saídas anunciadas também precisam de um mapa de funções/timers compatível com o firmware e os atuadores escolhidos.

Na documentação do 6X há diferenças de suporte entre revisões: Rev8 e Rev3/4 têm mínimos de firmware diferentes; é ainda assinalada uma incompatibilidade de Rev3/4 com ArduPilot 4.5.3. Verificar a revisão do equipamento efetivamente disponibilizado antes de o programar. [Compatibilidade por revisão](https://docs.holybro.com/autopilot/pixhawk-6x/supported-firmware).

**Critério de fecho:** aproveitar equipamento já existente se satisfizer os requisitos; comparar depois portas, atuadores, massa/dimensão, alimentação, suporte da revisão, disponibilidade e custo do conjunto. Os factos acima não estabelecem um vencedor sem esses dados. Não foi efetuada compra nem assumido preço.

## 5. Arquitetura inicial de ligações

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

### RC, telemetria e comunicações internas

- **RC:** transporta os comandos do piloto. SBUS e CRSF são alternativas da ligação recetor–controlador, não nomes da frequência usada pelo rádio. CRSF exige uma porta série adequada; confirmar pinagem, sinal e requisitos do recetor escolhido. [Sistemas RC ArduPilot](https://ardupilot.org/plane/docs/common-rc-systems.html).
- **Telemetria:** transporta estado, parâmetros e mensagens de missão/comando entre controlador e estação de terra. MAVLink é um protocolo candidato; UART é uma interface local, enquanto o rádio constitui o transporte sem fios. Alguns sistemas RC também transportam telemetria. [Telemetria ArduPilot](https://ardupilot.org/plane/docs/common-telemetry-landingpage.html).
- **Comunicações internas:** UART, I2C e CAN/DroneCAN dependem do periférico. A opção tem de caber no mapa de portas e no esquema elétrico. As características das portas do controlador escolhido prevalecem sobre um esquema genérico.

Proponho começar com controlo RC e telemetria tratados como funções distintas, para testar a perda de cada ligação separadamente. Frequência, potência, alcance, antenas e comportamento de falha ficam sujeitos às regras e à revisão da equipa.

Um `HEARTBEAT` MAVLink ajuda a identificar sistemas e a detetar ausência de mensagens esperadas; não demonstra por si só que todos os sensores ou o controlo de voo estejam saudáveis. O protocolo não fixa um prazo universal de perda de ligação: esse prazo terá de vir do requisito e da configuração. [Protocolo heartbeat](https://mavlink.io/en/services/heartbeat.html).

## 6. Divisão de trabalho a propor entre os responsáveis

| Área | Proposta para Software/Comunicações | Articulação necessária |
|---|---|---|
| Firmware e configuração | André e Rita escolhem o fluxo a avaliar, registam parâmetros e evidências. | Hardware confirma suporte e revisão da placa. |
| RC e telemetria | Software define mensagens, modos e comportamentos; identifica interfaces necessárias. | Hardware confirma alimentação, rádio, cabos e ligação física; piloto valida os comandos. |
| Sensores | Software define dados necessários e drivers/configuração a estudar. | Hardware seleciona a alimentação e a compatibilidade elétrica; Estruturas define implantação. |
| Atuadores | Software define funções/canais e valida o mapeamento em conjunto. | Hardware dimensiona servos/ESC e a alimentação; Mecânica confirma sentido e curso úteis. |
| Registo e testes | Software organiza cenários, logs, critérios e rastreabilidade. | Cada departamento valida os resultados relacionados com o seu subsistema. |

São propostas de divisão operacional; só as lideranças conjuntas ficaram atribuídas na 2.ª reunião. André não fica unilateralmente responsável por toda a eletrónica nem são atribuídas tarefas à Rita sem alinhamento com ela.

## 7. Progressão de validação proposta

1. **Simulação:** confirmar configuração, telemetria, mudanças de modo e cenários de perda de ligação com um modelo de teste.
2. **Bancada:** confrontar as interfaces com o equipamento real, verificar alimentação, leitura de sensores, canais e registos; ensaios de atuadores sem hélice e com movimentos controlados.
3. **Controlo manual:** validar a aeronave e o comando pelo piloto segundo o plano de ensaios da equipa.
4. **Assistência:** introduzir estabilização e outras funções apenas depois de validar configuração, sensores e transições.
5. **Autonomia:** executar as funcionalidades exigidas pela classe escolhida, com recuperação de controlo, limites e mecanismos de falha previamente definidos.

A passagem entre fases depende da revisão e dos resultados. Um ensaio SITL não demonstra compatibilidade elétrica, qualidade da ligação rádio ou aptidão para voo da aeronave real.

## 8. Primeiro ensaio SITL — guião pronto, ainda não executado

**Estado atual: não instalado/não executado neste trabalho.** Este guião usa o fluxo oficial ArduPilot; pressupõe um clone preparado e dependências disponíveis. A referência de versão a reproduzir é a indicada na secção 2, com o commit efetivamente utilizado registado no resultado.

Depois de preparado esse ambiente, no diretório do clone ArduPilot:

```bash
./Tools/autotest/sim_vehicle.py -v ArduPlane -f plane --console --map
```

O comando lança o modelo `plane` de estudo e MAVProxy. O modelo deverá ser alterado se a equipa aprovar outra configuração. O manual [Using SITL](https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html) descreve este fluxo e as opções para ligar outra GCS; o [guia Linux](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html) trata da preparação do ambiente. O modelo `plane` não é uma aprovação de asa fixa para o projeto.

### Critérios propostos e evidências a guardar

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

## 9. Decisões a fechar no próximo encontro

- Qual é a classe de competição e que configuração de aeronave está efetivamente em avaliação?
- Que controlador, rádio, sensores e computador existem já na equipa?
- Aceitamos ArduPlane como primeira opção para simulação, mantendo PX4 como alternativa documentada?
- Quem prepara o primeiro SITL e quem revê a matriz de interfaces com Hardware?
- Que dados, comportamento de falha e evidências são indispensáveis para o primeiro entregável?
- Como dividimos o trabalho entre André, Rita e os restantes elementos sem duplicar configurações?

**Resultado da pesquisa:** duas plataformas comparadas, duas placas concretas verificadas, arquitetura proposta, 14 interfaces preenchidas e critérios de ensaio preparados. A escolha da equipa e as evidências de execução continuam abertas.

## 10. Referências de outras equipas

Não consegui confirmar uma lista de componentes de uma equipa portuguesa da AeroCup nas fontes públicas consultadas. Os dois exemplos seguintes têm evidência primária; pertencem a contextos com missões e regulamentos diferentes dos da AeroCup.

**Beihang Aeromodelling Team — UAS Challenge 2026.** A universidade informa que a equipa integrou **ArduPilot num modelo de voo em X-Plane**, usando simulação iterativa antes e durante o desenvolvimento. O artigo é de 09/07/2026. Demonstra uma combinação concreta de autopiloto e simulador numa equipa universitária; não identifica uma placa que possamos adotar por comparação direta. [Relato oficial da Beihang University](https://ev.buaa.edu.cn/info/1022/3213.htm).

**CUAir — Cornell University, documentação de 2015–2016.** O repositório da própria equipa documenta utilizações específicas de **ArduPilot** e faz referência à calibração através do **Mission Planner**, com configuração de failsafe associada às suas regras de competição. É uma referência histórica de integração, não uma afirmação sobre o equipamento atual da equipa. A identidade universitária é confirmada no seu site. [Documentação técnica CUAir](https://github.com/CUAir/Autopilot/blob/master/docs/ardupilot.rst), [site da equipa](https://cuair.org/).

**Aplicação proposta ao ISEP:** aproveitar o método — simular, documentar configuração, registar resultados e confrontar falhas com os requisitos — mantendo a escolha da placa, os parâmetros e as regras próprios do nosso projeto. Estes exemplos sustentam o estudo de uma plataforma existente; não provam adequação automática à nossa aeronave.
