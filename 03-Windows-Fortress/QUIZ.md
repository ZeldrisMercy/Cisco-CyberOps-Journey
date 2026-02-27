# 🧠 Simulado Definitivo: Module 03 (Windows Fortress)

Estas 18 questões refletem as "pegadinhas" exatas de fóruns de discussão e simulados atualizados para o exame **Cisco CBROPS 200-201**.

---

### 🏛️ Domínio 1: Windows Internals e Memória

**1. No Windows, o que define a "Virtual Address Space" (Espaço de Endereço Virtual) alocada para um processo?**
- [ ] A) O espaço físico real no disco rígido reservado para o arquivo de paginação (pagefile.sys).
- [ ] B) O conjunto de endereços de memória virtuais que faz referência ao objeto de memória física que o processo tem permissão para usar.
- [ ] C) O limite máximo de threads que um aplicativo pode executar simultaneamente.
- [ ] D) A memória em cache do processador (L1/L2) alocada para o User Mode.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Questão clássica do exame. O espaço de endereço virtual é a ilusão que o SO cria para cada processo, fazendo-o pensar que tem blocos de memória contíguos e isolados à sua disposição.
</details>
<br>

**2. Na arquitetura Windows, qual termo descreve o objeto abstrato que um processo usa para obter acesso e interagir com um recurso do sistema, como uma porta de rede ou uma chave de registro?**
- [ ] A) Thread
- [ ] B) Hive
- [ ] C) Handle
- [ ] D) Token

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Handle)</b><br>
<i>Explicação:</i> Um "Handle" é um identificador (um ponteiro) que o Windows entrega ao processo para que ele possa acessar recursos sem precisar interagir diretamente com o hardware.
</details>
<br>

**3. Um driver de vídeo mal codificado tentou acessar uma área de memória não autorizada, resultando em uma Tela Azul da Morte (BSOD) e o travamento completo do SO. Em qual modo esse driver estava operando?**
- [ ] A) User Mode
- [ ] B) Safe Mode
- [ ] C) Kernel Mode
- [ ] D) HAL Mode

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Kernel Mode)</b><br>
<i>Explicação:</i> Falhas no Ring 0 (Kernel Mode) causam colapso total (panic) do sistema para proteger o hardware. Falhas no Ring 3 (User Mode) derrubariam apenas o aplicativo.
</details>

---

### 🛡️ Domínio 2: Endpoint Protection e Conceitos

**4. Qual é a principal vantagem de uma solução de segurança de endpoint baseada em agente (Agent-based) quando comparada a uma solução sem agente (Agentless)?**
- [ ] A) Ela elimina a necessidade de atualizações de software no sistema operacional.
- [ ] B) Ela consome zero recursos de CPU e memória do host.
- [ ] C) Ela possui visibilidade profunda dos processos em execução, chamadas de sistema e arquivos no disco local do host.
- [ ] D) Ela gerencia o tráfego de roteamento entre diferentes VLANs.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Como o agente é um software instalado *dentro* do Windows, ele pode ver exatamente o que está acontecendo na memória e nos processos internos. A solução Agentless monitora "de fora" (pela rede ou hipervisor).
</details>
<br>

**5. Uma empresa configurou suas políticas de segurança para que *nenhum* software executável (como um arquivo .exe novo) possa rodar nas máquinas dos funcionários, a menos que o hash ou o certificado desse software esteja em uma lista pré-aprovada pela TI. Que técnica é essa?**
- [ ] A) Application Blacklisting
- [ ] B) Signature-based Antivirus
- [ ] C) Host-Based Intrusion Prevention
- [ ] D) Application Whitelisting

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D (Whitelisting)</b><br>
<i>Explicação:</i> Whitelisting (Lista de Permissão) bloqueia tudo por padrão e só permite o que está aprovado, sendo uma defesa excepcional contra malwares de dia zero (Zero-day).
</details>
<br>

**6. Se um analista recebe um anexo de e-mail suspeito (um arquivo PDF que parece malicioso) e decide abri-lo em um ambiente virtual restrito para observar o comportamento do arquivo sem colocar a rede em risco, qual técnica ele está utilizando?**
- [ ] A) Sistemas de Whitelisting
- [ ] B) Systems-based Sandboxing
- [ ] C) Reverse Engineering
- [ ] D) Port Mirroring

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (Sandboxing)</b><br>
<i>Explicação:</i> O Sandboxing isola o arquivo em uma "caixa de areia" virtual onde ele pode ser detonado de forma segura, permitindo que a equipe estude seu comportamento (quais chaves de registro ele altera, pra quais IPs ele liga).
</details>

---

### 📁 Domínio 3: Sistema de Arquivos e Registro

**7. Uma técnica comum de evasão de defesas envolve anexar um payload malicioso a um arquivo inofensivo no sistema de arquivos NTFS, sem que o tamanho do arquivo original mude no Windows Explorer. Qual é o nome dessa funcionalidade?**
- [ ] A) Encrypting File System (EFS)
- [ ] B) Alternate Data Streams (ADS)
- [ ] C) Volume Shadow Copy
- [ ] D) BitLocker

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (ADS)</b><br>
<i>Explicação:</i> O Alternate Data Streams (ADS) permite que mais de um fluxo de dados seja associado a um único arquivo, uma técnica muito abusada para esconder rootkits e executáveis.
</details>
<br>

**8. Um malware deseja garantir persistência na máquina infectada de forma que, independente de qual funcionário faça o login no computador pela manhã, o malware inicie automaticamente. Em qual Hive do Registro do Windows o malware tentará escrever sua chave de inicialização?**
- [ ] A) HKEY_CURRENT_USER (HKCU)
- [ ] B) HKEY_LOCAL_MACHINE (HKLM)
- [ ] C) HKEY_CLASSES_ROOT (HKCR)
- [ ] D) HKEY_USERS (HKU)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (HKEY_LOCAL_MACHINE)</b><br>
<i>Explicação:</i> A HKLM contém configurações de hardware, software e serviços que afetam o sistema inteiro, sendo aplicadas em nível de máquina e não de usuário.
</details>
<br>

**9. Ao analisar as permissões NTFS de uma pasta, você nota permissões conflitantes. Um usuário pertence ao grupo "Vendas" (permissão de Leitura), mas também pertence ao grupo "Gerência" (permissão de Controle Total). Qual será o acesso efetivo do usuário?**
- [ ] A) O Windows bloqueará o acesso.
- [ ] B) Leitura (O Windows aplica a permissão mais restritiva).
- [ ] C) Controle Total.
- [ ] D) Depende de qual grupo o usuário entrou primeiro.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Controle Total)</b><br>
<i>Explicação:</i> No NTFS, permissões de concessão (Allow) são cumulativas. O usuário herda a maior permissão possível. A exceção é o Deny explícito, que sempre vence qualquer Allow.
</details>

---

### 💻 Domínio 4: Sysinternals e Ferramentas Nativas

**10. Você precisa investigar qual executável do Windows está abrindo uma conexão suspeita na porta TCP 4444 para um IP externo. Qual comando no prompt (CMD) fornecerá o nome do processo e o seu PID, juntamente com o status da rede?**
- [ ] A) `netstat -abno`
- [ ] B) `ipconfig /displaydns`
- [ ] C) `nslookup`
- [ ] D) `tracert -d`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A (`netstat -abno`)</b><br>
<i>Explicação:</i> O parâmetro `-a` mostra conexões ativas; `-b` mostra o executável; `-n` mostra IPs numéricos; e `-o` exibe o PID do processo.
</details>
<br>

**11. Usando a ferramenta Process Explorer (da suíte Sysinternals), um analista clica com o botão direito em um processo chamado "svchost.exe" e seleciona "Verify Image Signatures". O que ele está fazendo?**
- [ ] A) Fazendo upload do arquivo para o antivírus local.
- [ ] B) Verificando se o executável foi assinado digitalmente por um fornecedor confiável (como a Microsoft), ajudando a detectar malwares disfarçados.
- [ ] C) Criptografando a memória do processo.
- [ ] D) Interrompendo as threads dependentes do processo.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Se o arquivo "svchost.exe" der "Unverified" ou "No signature", é quase certo que se trata de um malware tentando se passar por um processo vital do sistema operacional.
</details>

---

### 📊 Domínio 5: Log Analysis e Event Viewer

**12. O SIEM gerou um alerta severo ao detectar a seguinte sequência no servidor: Vinte logs seguidos com o Event ID 4625, culminando imediatamente em um log com o Event ID 4624 para o mesmo usuário. O que ocorreu?**
- [ ] A) Um ataque de DDoS volumétrico no servidor web.
- [ ] B) Um ataque de força bruta (Brute Force) de senhas bem-sucedido.
- [ ] C) Uma desativação e reativação do serviço de antivírus.
- [ ] D) Um escalonamento de privilégios via PowerShell.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Event ID 4625 = Falha de Logon. Event ID 4624 = Logon Bem-sucedido. Dezenas de falhas seguidas de um acerto são a impressão digital de um script testando senhas (Brute-Force ou Password Spraying).
</details>
<br>

**13. Ao revisar os logs de segurança do Windows (Event Viewer) após uma suspeita de intrusão, o analista descobre que as entradas das últimas 48 horas estão completamente vazias, e há um registro único do Event ID 1102. O que isso significa?**
- [ ] A) O disco rígido apresentou falhas de escrita.
- [ ] B) O atacante apagou (limpou) intencionalmente o log de auditoria do Windows para esconder seus rastros.
- [ ] C) O servidor foi reiniciado no modo de segurança.
- [ ] D) O serviço de backup fez o arquivamento dos logs.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O Event ID 1102 sinaliza "The audit log was cleared". O próprio ato de apagar os logs gera esse evento, alertando o SOC de que alguém tentou encobrir uma ação maliciosa.
</details>
<br>

**14. A detecção da execução de malwares é um desafio. Qual Event ID do Windows o analista de SOC deve configurar para ser enviado ao SIEM caso ele queira monitorar o momento exato em que um novo processo (Process Creation) é iniciado no sistema operacional?**
- [ ] A) 4624
- [ ] B) 4688
- [ ] C) 7040
- [ ] D) 5140

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (4688)</b><br>
<i>Explicação:</i> O Event ID 4688 documenta a criação de um novo processo. Se devidamente configurado nas GPOs com o recurso de "Command Line auditing", o analista consegue ver não apenas o processo, mas os argumentos exatos que o atacante digitou.
</details>

---

### ⚙️ Domínio 6: Políticas e Infraestrutura

**15. Em um domínio corporativo (Active Directory), qual é a ferramenta nativa principal que permite impor configurações de segurança complexas, desabilitar o painel de controle e mapear unidades de rede para todos os computadores da empresa simultaneamente?**
- [ ] A) Local Security Policy (secpol.msc)
- [ ] B) Windows Management Instrumentation (WMI)
- [ ] C) Group Policy Object (GPO)
- [ ] D) Sysinternals Suite

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (GPO)</b><br>
<i>Explicação:</i> As GPOs permitem o controle centralizado do domínio, empurrando configurações para todos os endpoints. O `secpol.msc` faria isso máquina por máquina (inviável em redes grandes).
</details>
<br>

**16. O administrador utiliza o UAC (User Account Control). Em qual momento o UAC protege o sistema operacional contra elevação de privilégios silenciosa por um malware?**
- [ ] A) Ele criptografa a tabela de roteamento local.
- [ ] B) Ele exige uma confirmação do usuário (um prompt na tela) antes de permitir que um executável faça alterações de nível administrativo.
- [ ] C) Ele bloqueia o acesso à internet para processos não assinados.
- [ ] D) Ele desinstala softwares que não pertencem à Microsoft.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O UAC escurece a tela e exige aprovação (ou senha de admin). Isso quebra a execução silenciosa de malwares que tentam se instalar no background utilizando os privilégios do usuário logado.
</details>
<br>

**17. O processo `lsass.exe` (Local Security Authority Subsystem Service) é frequentemente atacado com ferramentas de extração de memória como o Mimikatz. Qual é a principal função deste processo?**
- [ ] A) Gerenciar a resolução de nomes de domínio (DNS).
- [ ] B) Gerenciar políticas de segurança local, autenticação e armazenar credenciais/hashes na memória RAM.
- [ ] C) Prover os serviços de spooler de impressão.
- [ ] D) Executar as rotinas de criptografia do BitLocker.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O `lsass.exe` lida com o login no Windows e a criação do Token de Acesso do usuário. É o principal alvo para "Credential Dumping" (Roubo de Credenciais).
</details>
<br>

**18. O que caracteriza um malware "Fileless" (sem arquivo) e por que ele utiliza ferramentas nativas como o PowerShell e o WMI (Living off the Land)?**
- [ ] A) Ele é hospedado exclusivamente na nuvem e ataca via DDoS.
- [ ] B) Ele é injetado e executado diretamente na memória RAM, utilizando binários legítimos do SO, não deixando artefatos (como arquivos .exe) no disco para o antivírus comum detectar.
- [ ] C) Ele opera apenas alterando o firmware da placa-mãe.
- [ ] D) Ele exclui os arquivos do usuário após a infecção.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O Fileless Malware explora as ferramentas do próprio Windows (PowerShell, WMI) para rodar o ataque na memória, burlando as defesas baseadas em assinaturas de arquivos no disco.
</details>
