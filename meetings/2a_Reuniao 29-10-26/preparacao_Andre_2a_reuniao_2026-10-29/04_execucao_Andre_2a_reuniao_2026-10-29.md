# UAS 2027 — 2.ª reunião — 29/10/2026 — Plano de execução de André

**Papel confirmado:** liderança conjunta de Software/Comunicações com Rita. Hardware é liderado por Eduardo e Beatriz. **Base:** resumo da 2.ª reunião, em especial 32:11–32:33. **Estado deste plano:** proposta de execução preparada após a reunião; os responsáveis e os prazos abaixo precisam de alinhamento com a equipa.

## 1. Trabalho de preparação já executado

| Pedido da reunião | Entregável preparado | O que falta para o fechar com a equipa |
|---|---|---|
| Ler as regras relevantes | Síntese das regras e matriz de requisitos, com secções, fontes e verificação proposta | Confirmar classe e aplicabilidade; rever os requisitos em conjunto. |
| Investigar soluções | Comparação ArduPilot/PX4, estações de controlo e candidatos de hardware | Confirmar configuração, material existente e restrições; escolher a solução. |
| Articular Hardware e Software | Arquitetura funcional e matriz de interfaces preenchida | Fechar sinais, alimentação, conectores, versões e responsabilidades. |
| Reunir empresas e contactos | Sete entidades pesquisadas e folha de contactos | Encaminhar para a área de empresas/patrocínios e escolher os pedidos. |
| Organizar o departamento | Proposta de divisão, tarefas e critérios de conclusão | Rita e restantes membros participam na distribuição final. |
| Preparar o próximo encontro | Pauta de 45 minutos, perguntas e textos de contacto prontos | Confirmar participantes, disponibilidades, dia, hora e plataforma. |

Os documentos estão preparados para discussão. Ensaios, implementação, compras e aceitação da equipa têm estados próprios e permanecem pendentes.

## 2. Ordem de execução a partir daqui

### P0 — Fechar o contexto com Rita e coordenação

**Proposta para André:** usar os textos do documento de mensagens para alinhar três assuntos: membros do departamento, classe de competição e acessos. A reunião já definiu as lideranças; a conversa seguinte deve avançar para trabalho concreto.

Resultados necessários:

- Saber quem entrou em Software/Comunicações após a votação.
- Ter o acesso ao grupo/Discord e ao local dos documentos.
- Confirmar com a coordenação a classe inscrita ou pretendida e a configuração da aeronave em estudo.
- Confirmar quem é o representante global da equipa perante a AeroCup e quem acompanha inscrição e entregas.
- Saber se existe controlador, rádio, recetor, sensores, computador de bancada ou outro material aproveitável.
- Recolher a disponibilidade real dos membros para a reunião por departamento.

**Critério de conclusão:** estas respostas ficam registadas no documento de decisões e na folha de tarefas. A data da reunião só é fechada depois de cruzar disponibilidades.

### P1 — Apresentar uma primeira base técnica já preenchida

**Proposta de divisão inicial, a acordar:** André começa pela manutenção dos requisitos, interfaces e documentação de ensaios; Rita escolhe a área que prefere aprofundar, por exemplo comunicações/GCS ou comparação das plataformas. A proposta usa o trabalho de preparação já disponível e permite redistribuição segundo experiência e disponibilidade.

Na primeira conversa de trabalho, apresentar:

1. A matriz de requisitos, com cada regra ligada à respetiva fonte e a um método de verificação.
2. A arquitetura candidata comum ao voo manual e à evolução autónoma.
3. A matriz de interfaces, destacando as respostas necessárias de Hardware.
4. A comparação de plataformas, com uma recomendação de estudo e as alternativas.

**Critério de conclusão:** requisitos aceites ou corrigidos; dúvidas com responsável; decisão de plataforma registada ou uma lista curta de informação que falta para decidir.

### P2 — Fechar as interfaces com Eduardo e Beatriz

Levar a matriz de interfaces para a conversa de integração. Os pontos de maior impacto são alimentação da eletrónica, ligações entre recetor e controlador, saídas para atuadores, sensores, telemetria e espaço/massa para integração na estrutura.

**Critério de conclusão:** para cada ligação crítica, existe uma função definida, um interlocutor em cada departamento e um registo dos dados elétricos/mecânicos ainda por fechar. A matriz contém as ligações a discutir; os protocolos candidatos precisam de validação.

### P3 — Fazer a primeira demonstração de software

**Proposta:** começar em simulação/bancada pela comunicação entre controlador simulado e estação de controlo, pela observação dos modos/estado e pela recolha de um registo de ensaio. O documento de arquitetura contém o roteiro e os casos a observar.

A execução depende da plataforma escolhida e do computador disponível. O pacote atual deixa o roteiro preparado; não contém resultados de um simulador ou de hardware que tenha sido ensaiado.

**Evidência a produzir quando o ensaio for executado:** versões utilizadas, configuração, caso executado, resultado esperado e observado, log e conclusão. Uma ligação estabelecida ou um heartbeat observado demonstram conectividade naquele ensaio; os requisitos de controlo e de falha precisam dos seus próprios testes.

### P4 — Encaminhar a pesquisa de empresas

Entregar a folha preenchida à área de empresas/patrocínios. Essa área confirma contactos anteriores e escolhe a abordagem; André e Rita fornecem o pedido técnico. A lista prepara o trabalho de contacto, sem pressupor interesse ou apoio das entidades.

## 3. Entregável a propor para o primeiro ciclo do departamento

**Proposta:** baseline inicial de Software/Comunicações, versão 0.1, composta por requisitos aplicáveis, diagrama funcional, interfaces críticas e plano de um primeiro ensaio em simulação.

Critérios de aceitação propostos:

- Cada requisito tem origem, aplicabilidade e forma de verificação identificadas.
- As escolhas técnicas aprovadas ficam separadas das opções em avaliação.
- Cada interface crítica tem interlocutores e pendências registadas.
- O primeiro ensaio tem ambiente, resultado esperado e evidência a guardar definidos.
- André e Rita revêm a baseline; Hardware valida as interfaces que lhe dizem respeito.

O prazo deve ser combinado no primeiro encontro. Este documento propõe o conteúdo e os critérios; a reunião de 29/10 não fixou uma data de entrega para esta baseline.

## 4. O que precisas de compreender antes de apresentar o trabalho

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

## 5. Riscos de planeamento e resposta proposta

| Tema | Consequência prática | Resposta proposta |
|---|---|---|
| Classe ou configuração ainda em aberto | Requisitos e interfaces podem mudar | Fechar com a coordenação; identificar aplicabilidade condicional na matriz. |
| Material disponível desconhecido | Comparar compras que talvez sejam desnecessárias | Pedir inventário antes da seleção. |
| Interfaces elétricas indefinidas | Incompatibilidades e retrabalho na integração | Rever a matriz com Hardware antes de ligar componentes. |
| Dois departamentos a estudar o mesmo problema | Trabalho duplicado | André/Rita e Eduardo/Beatriz atribuem um responsável por assunto e partilham resultados. |
| Versões não registadas | Ensaios difíceis de repetir | Guardar versões, configuração e logs por ensaio. |
| Disponibilidade ainda não recolhida | Reunião e tarefas sem responsáveis efetivos | Cruzar disponibilidades e atribuir tarefas pequenas com critérios claros. |

## 6. Dependências pessoais e externas

O trabalho de pesquisa e os documentos já estão preparados. As respostas que ainda precisam de vir de pessoas são: a tua disponibilidade, a preferência de Rita na divisão de tarefas, a composição final do grupo, os acessos, o inventário, a classe/configuração e a aceitação das propostas.

A [folha de tarefas](tarefas_2a_reuniao_2026-10-29.csv) distingue preparação concluída, propostas por rever e dependências externas. A pauta e os textos estão no [documento de mensagens e reunião](05_mensagens_pauta_2a_reuniao_2026-10-29.md).

## 7. Pontos administrativos para a coordenação

O Handbook 2027, v1.0, secções 2.4.1 e 3.1, prevê um representante global da equipa e indica o fim das inscrições em **21/01/2027 às 23:59**, com lugares limitados. O fuso desse prazo não está explicitado nessa passagem. A co-liderança de um departamento não identifica, por si, esse representante. André deve obter a confirmação do estado da inscrição e do interlocutor; a administração geral continua com a coordenação. [Handbook oficial](https://firebasestorage.googleapis.com/v0/b/aerocup-website.firebasestorage.app/o/public%2FAeroCup_2027_Handbook_v1_0.pdf?alt=media&token=e7ad08ae-707b-469c-875d-38f947bcdf6e).

O site anuncia 8–12 de julho de 2027; o Handbook inclui 13 de julho como dia de partida. Confirmar mais perto do evento os dias necessários para logística. Esta informação não altera o estado do próximo encontro do departamento, que continua sem dia e hora fixados. [Site oficial](https://aerocup.pt/).
