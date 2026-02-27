# 🧠 Simulado: Module 01 (The Danger & Security Concepts)

Bem-vindo ao simulador de exames. Estas 15 questões foram elaboradas nos mesmos moldes da certificação oficial **Cisco CyberOps Associate (200-201)**. 

**Instruções:** Leia o cenário, escolha sua alternativa (A, B, C ou D) e clique no botão de gabarito para verificar sua resposta e ler a explicação técnica.

---

### 🛡️ Domínio 1: Princípios de Segurança e Controle de Acesso

**1. Um ataque volumétrico de negação de serviço (DDoS) satura a banda de internet de um hospital, impedindo que os médicos acessem o portal de prontuários em nuvem. Qual princípio da Tríade CIA foi comprometido?**
- [ ] A) Confidencialidade
- [ ] B) Integridade
- [ ] C) Disponibilidade
- [ ] D) Autenticação

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Disponibilidade)</b><br>
<i>Explicação:</i> Os dados não foram vazados (Confidencialidade) nem alterados (Integridade). O ataque visa exclusivamente derrubar o acesso legítimo ao sistema, ferindo a Disponibilidade (Availability).
</details>

<br>

**2. O sistema de arquivos de uma agência de inteligência impõe regras rígidas baseadas em rótulos como "Secreto" e "Top Secret". Um usuário com acesso "Secreto" tenta ler um arquivo "Top Secret", mas é bloqueado pelo sistema operacional, mesmo que o criador do arquivo queira liberar o acesso. Qual modelo de controle de acesso é esse?**
- [ ] A) DAC (Discretionary Access Control)
- [ ] B) MAC (Mandatory Access Control)
- [ ] C) RBAC (Role-Based Access Control)
- [ ] D) ABAC (Attribute-Based Access Control)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (MAC)</b><br>
<i>Explicação:</i> No MAC, o sistema impõe (mandatório) o acesso baseado em rótulos de confidencialidade, ignorando a vontade do proprietário do arquivo. No DAC, o dono decide; no RBAC, o cargo decide.
</details>

<br>

**3. Qual componente do framework AAA é acionado quando um analista de segurança consulta o arquivo `/var/log/auth.log` para verificar quantos comandos `sudo` um usuário executou durante a noite?**
- [ ] A) Authentication (Autenticação)
- [ ] B) Authorization (Autorização)
- [ ] C) Accounting (Auditoria/Contabilização)
- [ ] D) Availability (Disponibilidade)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Accounting)</b><br>
<i>Explicação:</i> Accounting refere-se a registrar, auditar e rastrear o que o usuário fez após ser autenticado e autorizado no sistema.
</details>

<br>

**4. Na taxonomia de segurança corporativa, como é chamada a prática de sobrepor várias tecnologias de defesa (ex: Firewall + IPS + EDR + MFA) para que a falha de uma não comprometa toda a rede?**
- [ ] A) Zero Trust Network Access
- [ ] B) Separation of Duties
- [ ] C) Principle of Least Privilege
- [ ] D) Defense in Depth (Defesa em Profundidade)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D (Defense in Depth)</b><br>
<i>Explicação:</i> Defesa em Profundidade é a arquitetura em camadas (como os muros de um castelo). Se o atacante passar pelo fosso (Firewall), ainda terá que lidar com os guardas (IPS) e as portas trancadas (EDR).
</details>

---

### 💀 Domínio 2: Atores de Ameaça e Engenharia Social

**5. Um grupo de invasores invade os servidores de uma refinaria de petróleo. Em vez de exigir resgate financeiro, eles permanecem furtivos na rede por meses, mapeando processos industriais para fins de espionagem patrocinada por um país rival. Qual é a classificação mais precisa desse grupo?**
- [ ] A) Hacktivistas
- [ ] B) Script Kiddies
- [ ] C) APT (Advanced Persistent Threat)
- [ ] D) Insider Threat

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (APT)</b><br>
<i>Explicação:</i> Atores APTs (frequentemente patrocinados por governos/State-Sponsored) possuem vastos recursos e seu principal objetivo é a persistência e a extração de dados a longo prazo, não o ganho financeiro rápido.
</details>

<br>

**6. O CFO (Diretor Financeiro) de uma multinacional recebe um e-mail aparentemente do CEO, solicitando uma transferência bancária urgente e confidencial para fechar a compra de uma startup. O e-mail contém linguagem formal típica da empresa. Qual é o nome específico deste ataque?**
- [ ] A) Vishing
- [ ] B) Whaling
- [ ] C) Pharming
- [ ] D) Baiting

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (Whaling)</b><br>
<i>Explicação:</i> Whaling (Caça às Baleias) é um tipo específico de Spear Phishing altamente direcionado a executivos do alto escalão (C-Level), explorando a autoridade de seus cargos.
</details>

<br>

**7. Um funcionário revoltado com sua demissão iminente instala um software de limpeza de disco no servidor de banco de dados para rodar automaticamente na sexta-feira à noite e apagar todos os backups. Como classificamos a ameaça e o tipo de malware?**
- [ ] A) Insider Threat / Ransomware
- [ ] B) Hacktivista / Rootkit
- [ ] C) APT / Trojan
- [ ] D) Insider Threat / Logic Bomb

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D (Insider Threat / Logic Bomb)</b><br>
<i>Explicação:</i> O funcionário é uma ameaça interna (Insider). O malware é uma Bomba Lógica (Logic Bomb), pois foi programado para "detonar" apenas quando uma condição específica for atendida (chegar na sexta-feira à noite).
</details>

<br>

**8. O grupo de ransomware que atacou a sua empresa não criptografou os arquivos, mas roubou os bancos de dados de clientes e ameaça publicá-los em um fórum na dark web caso o pagamento não seja feito. Qual tática do Kill Chain e qual princípio da CIA estão em foco?**
- [ ] A) Exploitation / Disponibilidade
- [ ] B) Exfiltração / Confidencialidade
- [ ] C) Reconhecimento / Integridade
- [ ] D) Delivery / Disponibilidade

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (Exfiltração / Confidencialidade)</b><br>
<i>Explicação:</i> Roubar dados da rede para o mundo externo é Exfiltração. Como a ameaça é tornar os dados públicos, o princípio violado é a Confidencialidade (vazamento duplo/double extortion).
</details>

---

### 🌐 Domínio 3: Vetores de Ataque e Classificação de Dados

**9. Analisando o incidente "Aupticon", nota-se que o invasor não atacou a empresa diretamente. Ele identificou que os engenheiros da empresa visitavam o site de uma liga de boliche e injetou um código malicioso lá. Como se chama este vetor de ataque?**
- [ ] A) Watering Hole Attack
- [ ] B) Man-in-the-Middle (MitM)
- [ ] C) Cross-Site Scripting (XSS)
- [ ] D) SQL Injection

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A (Watering Hole Attack)</b><br>
<i>Explicação:</i> No ataque do "bebedouro" (Watering Hole), o atacante compromete um site de terceiros amplamente confiável e visitado pelo seu alvo real, aguardando que as vítimas se infectem sozinhas.
</details>

<br>

**10. Uma clínica de psicologia foi invadida e os prontuários contendo diagnósticos e anotações de sessões dos pacientes foram vazados. De acordo com as leis de conformidade (como HIPAA ou LGPD), qual classificação exata esses dados recebem?**
- [ ] A) PII (Personally Identifiable Information)
- [ ] B) PCI (Payment Card Information)
- [ ] C) PSI (Personal Security Information)
- [ ] D) PHI (Protected Health Information)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D (PHI)</b><br>
<i>Explicação:</i> Embora diagnósticos também sejam dados sensíveis ligados a uma pessoa (PII), eles possuem uma classificação legal específica e muito mais rigorosa chamada PHI (Informações Protegidas de Saúde).
</details>

<br>

**11. Qual é a principal diferença entre uma Vulnerabilidade e um Risco de Cibersegurança?**
- [ ] A) Vulnerabilidade é o hacker; Risco é o malware que ele usa.
- [ ] B) Risco é a falha no sistema; Vulnerabilidade é o impacto financeiro.
- [ ] C) Vulnerabilidade é a fraqueza do sistema; Risco é a probabilidade dessa fraqueza ser explorada vezes o impacto gerado.
- [ ] D) Não há diferença técnica entre os termos na norma ISO 27001.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Risco = (Probabilidade da Ameaça explorar a Vulnerabilidade) x Impacto. A vulnerabilidade é apenas a porta destrancada; o risco mede quão perigoso é deixar essa porta aberta naquele contexto.
</details>

<br>

**12. Em um aeroporto, um atacante levanta um ponto de acesso Wi-Fi falso chamado "Aeroporto_Free_WiFi", o mesmo nome da rede legítima do local. O objetivo é fazer os celulares se conectarem a ele para roubar credenciais. Esse ataque é um exemplo clássico de:**
- [ ] A) Wardriving
- [ ] B) Evil Twin
- [ ] C) Bluejacking
- [ ] D) MAC Spoofing

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (Evil Twin)</b><br>
<i>Explicação:</i> O "Gêmeo Maligno" clona o SSID (nome da rede) legítimo para atuar como um roteador falso e executar um ataque Man-in-the-Middle silencioso contra os usuários que se conectam a ele.
</details>

---

### 📊 Domínio 4: Avaliação CVSS e Tipos de Malware

**13. Ao avaliar a métrica Base do CVSS v3.1 para uma nova vulnerabilidade, o analista verifica que o "Attack Vector (AV)" está classificado como "Network". O que isso significa para a equipe de resposta a incidentes?**
- [ ] A) A vulnerabilidade só pode ser explorada se o atacante estiver fisicamente na sede da empresa.
- [ ] B) A vulnerabilidade é crítica, pois pode ser explorada remotamente pela internet.
- [ ] C) O atacante precisa já ter uma conta na rede local (LAN) para explorar a falha.
- [ ] D) A falha só afeta equipamentos de infraestrutura (Switches e Roteadores).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> No CVSS, AV: Network (Rede) indica o pior cenário possível: a falha pode ser acionada remotamente, de qualquer lugar do mundo, sem necessidade de acesso físico ou de estar em uma sub-rede local.
</details>

<br>

**14. Qual tipo de malware é projetado especificamente para modificar o kernel do sistema operacional com o objetivo de esconder sua própria existência e a de outros malwares dos softwares de antivírus?**
- [ ] A) Ransomware
- [ ] B) Keylogger
- [ ] C) Rootkit
- [ ] D) Worm

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Rootkit)</b><br>
<i>Explicação:</i> O Rootkit se instala profundamente no sistema (geralmente em nível de Ring 0 / Kernel), interceptando as chamadas do sistema operacional para mentir ao antivírus, ocultando arquivos, portas abertas e processos em execução.
</details>

<br>

**15. Após a descoberta de uma vulnerabilidade de dia zero (Zero-Day) em um servidor web Apache, o fabricante lança uma atualização (Patch) de correção. Qual métrica do sistema de pontuação CVSS será alterada com o lançamento deste patch?**
- [ ] A) Métrica Base (Base Score)
- [ ] B) Métrica Ambiental (Environmental Score)
- [ ] C) Métrica Temporal (Temporal Score)
- [ ] D) Métrica de Impacto (Impact Score)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Métrica Temporal)</b><br>
<i>Explicação:</i> A Métrica Temporal reflete características da vulnerabilidade que mudam com o tempo. A disponibilidade de uma solução (Remediation Level), como a liberação de um patch oficial, reduz a pontuação temporal do risco.
</details>
