# 🧠 Simulado: Module 02 (Cybersecurity Professionals & SOC)

Bem-vindo ao simulador de exames. Estas 15 questões focam na operação de um SOC, uso de SIEM/SOAR e no ciclo de resposta a incidentes (NIST), conceitos altamente cobrados na certificação **Cisco CBROPS 200-201**.

---

### 🏛️ Domínio 1: Estrutura do SOC e Tecnologias

**1. Um analista recebe logs de um servidor Linux (formato Syslog), de um firewall Cisco (formato proprietário) e de um servidor Windows (Event Logs). Qual função do SIEM é responsável por traduzir todos esses dados brutos para um formato padronizado e pesquisável?**
- [ ] A) Correlação (Correlation)
- [ ] B) Agregação (Aggregation)
- [ ] C) Normalização (Normalization)
- [ ] D) Retenção (Retention)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Normalização)</b><br>
<i>Explicação:</i> A normalização é o processo de pegar campos diferentes (como "Source_IP", "src_ip", "IP_Origem") e padronizá-los em um único esquema para que o analista possa fazer buscas globais.
</details>
<br>

**2. O analista percebe que o SIEM gerou um alerta porque três eventos distintos aconteceram em um intervalo de 5 minutos: (1) O IPS detectou um scan de portas, (2) O firewall permitiu uma conexão RDP e (3) O Windows Defender alertou sobre a desativação do antivírus. Qual recurso do SIEM uniu essas peças?**
- [ ] A) Normalização
- [ ] B) Correlação
- [ ] C) Automação de Runbook
- [ ] D) Agregação

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (Correlação)</b><br>
<i>Explicação:</i> A correlação é a "mágica" do SIEM. Ela usa regras lógicas para conectar eventos aparentemente não relacionados de diferentes fontes de log, indicando um comportamento malicioso em andamento.
</details>
<br>

**3. Qual é a principal diferença operacional entre um SIEM e um SOAR em um SOC moderno?**
- [ ] A) O SIEM gera alertas passivos baseados em logs; o SOAR executa ações ativas de mitigação de forma automatizada.
- [ ] B) O SIEM é usado apenas para redes Linux, enquanto o SOAR foca no Active Directory.
- [ ] C) O SOAR substitui o firewall, enquanto o SIEM substitui o antivírus.
- [ ] D) Não há diferença; são termos diferentes para o mesmo software.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A</b><br>
<i>Explicação:</i> O SOAR (Security Orchestration, Automation, and Response) interage via APIs com firewalls e EDRs para isolar máquinas ou bloquear IPs automaticamente sem intervenção humana, algo que o SIEM tradicional não faz.
</details>
<br>

**4. Em um SOC de modelo estruturado, qual é a responsabilidade primária de um Analista Tier 1?**
- [ ] A) Realizar engenharia reversa de malwares complexos de Zero-Day.
- [ ] B) Fazer Threat Hunting proativo, caçando ameaças que passaram pelo SIEM.
- [ ] C) Monitorar a fila de alertas, realizar a triagem inicial e distinguir incidentes reais de falsos positivos.
- [ ] D) Projetar a arquitetura de novas regras de firewall corporativo.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> O Tier 1 atua na linha de frente (Triage). Ele avalia alertas constantes, fecha os que são Falsos Positivos e escala os incidentes confirmados para o Tier 2 (Resposta a Incidentes).
</details>
<br>

**5. Qual profissional do SOC não depende de alertas gerados por ferramentas de segurança para iniciar seu trabalho, assumindo que a rede já está comprometida?**
- [ ] A) SOC Manager
- [ ] B) Analista Tier 1
- [ ] C) Threat Hunter (SME)
- [ ] D) Engenheiro de Redes

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Threat Hunter)</b><br>
<i>Explicação:</i> A Caça a Ameaças (Threat Hunting) é uma atividade estritamente *proativa*. O analista procura por anomalias sutis e comportamentos furtivos (stealth) que escaparam das regras do SIEM e dos alertas do EDR.
</details>

---

### 📈 Domínio 2: Métricas de Segurança

**6. Após uma invasão de Ransomware, o Diretor de TI questiona quanto tempo a equipe levou para retirar fisicamente o cabo de rede e desativar a porta do switch do servidor infectado, impedindo que o malware criptografasse outras VLANs. Qual métrica mede especificamente esse esforço?**
- [ ] A) MTTD (Mean Time to Detect)
- [ ] B) MTTC (Mean Time to Contain)
- [ ] C) Dwell Time
- [ ] D) MTTR (Mean Time to Recover)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (MTTC)</b><br>
<i>Explicação:</i> O tempo para *Conter* o ataque ("estancar o sangramento" ou isolar o host) é o MTTC. O MTTR englobaria o tempo de formatar o servidor e voltar o backup, que ocorre após a contenção.
</details>
<br>

**7. A métrica "Dwell Time" (Tempo de Permanência) é calculada medindo o tempo entre quais dois eventos?**
- [ ] A) Do momento da infecção inicial até a detecção do invasor pelo SOC.
- [ ] B) Da detecção do invasor até a sua expulsão total da rede.
- [ ] C) Do momento em que o alerta apita no SIEM até o analista abrir o ticket.
- [ ] D) Do início da restauração do backup até o sistema voltar ao ar.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A</b><br>
<i>Explicação:</i> Dwell Time é o tempo em que o atacante fica "morando" livremente e de forma invisível dentro da rede. Ele começa na infecção (Exploitation) e termina apenas quando a equipe de defesa percebe a anomalia (Detecção).
</details>

---

### 🛡️ Domínio 3: Ciclo de Resposta a Incidentes (NIST SP 800-61)

**8. De acordo com o framework de Resposta a Incidentes do NIST, a criação de Playbooks, o treinamento dos analistas e a garantia de que as licenças de software forense estão atualizadas ocorrem em qual fase?**
- [ ] A) Preparação (Preparation)
- [ ] B) Detecção e Análise (Detection & Analysis)
- [ ] C) Contenção (Containment)
- [ ] D) Atividades Pós-Incidente (Post-Incident Activity)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A (Preparação)</b><br>
<i>Explicação:</i> A preparação é considerada a fase mais vital. Se o SOC não tiver os acessos, ferramentas configuradas e treinamentos em dia antes do incidente ocorrer, a resposta falhará.
</details>
<br>

**9. Durante um incidente envolvendo o roubo de senhas por um cavalo de troia (Trojan), a equipe de segurança executa um script que força a redefinição de todas as senhas dos usuários do Active Directory e deleta o executável malicioso do sistema. Em qual fase do ciclo NIST a equipe está operando?**
- [ ] A) Preparação
- [ ] B) Detecção
- [ ] C) Erradicação (Eradication)
- [ ] D) Lições Aprendidas (Lessons Learned)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Erradicação)</b><br>
<i>Explicação:</i> A erradicação visa eliminar os componentes da ameaça da rede. Deletar malwares, fechar portas que o atacante abriu e resetar credenciais comprometidas fazem parte desta fase.
</details>
<br>

**10. Após resolver um incidente massivo de Phishing, o SOC convoca uma reunião com o RH e a TI. É decidido que o RH fará treinamentos trimestrais contra Phishing e a TI bloqueará macros no pacote Office. Em qual fase do NIST essa reunião ocorre?**
- [ ] A) Contenção
- [ ] B) Detecção
- [ ] C) Erradicação
- [ ] D) Atividade Pós-Incidente (Post-Incident Activity)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D (Pós-Incidente)</b><br>
<i>Explicação:</i> Também conhecida como "Lições Aprendidas" (Lessons Learned). O objetivo é usar a experiência do ataque para melhorar políticas, afinar o SIEM e evitar que o mesmo tipo de incidente aconteça novamente.
</details>
<br>

**11. No modelo NIST, o ato de transferir um servidor web infectado para uma VLAN isolada que não possui comunicação com o banco de dados interno da empresa é um exemplo de:**
- [ ] A) Recuperação
- [ ] B) Detecção
- [ ] C) Contenção (Containment)
- [ ] D) Erradicação

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Contenção)</b><br>
<i>Explicação:</i> A contenção não resolve o problema do servidor web (ele continua infectado), mas impede que o atacante consiga fazer um Movimento Lateral para atingir os servidores de Banco de Dados.
</details>
<br>

**12. Qual é a utilidade de um "Playbook" na operação de um SOC?**
- [ ] A) Traduzir logs de firewall para linguagem humana.
- [ ] B) Fornecer um guia passo a passo padronizado para que os analistas saibam como responder a tipos específicos de incidentes (ex: Infecção por Ransomware).
- [ ] C) Descriptografar arquivos bloqueados por adversários.
- [ ] D) Substituir a equipe de Tier 1 através de Inteligência Artificial.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Playbooks (ou Manuais de Procedimentos) são vitais para a fase de Processos do SOC. Eles garantem que todos os analistas sigam o mesmo fluxo de contenção e coleta de evidências, mantendo a consistência jurídica e técnica da resposta.
</details>

---

### 🧩 Domínio 4: Conceitos Operacionais Mistos

**13. Você é um analista monitorando eventos e recebe uma lista de IoCs (Indicators of Compromise) enviada por uma agência de inteligência governamental sobre um novo grupo hacker. Qual dos itens abaixo é o exemplo perfeito de um IoC tático?**
- [ ] A) O nome do país que está patrocinando o ataque.
- [ ] B) A motivação financeira do grupo criminoso.
- [ ] C) Uma lista de hashes SHA-256 e endereços IP de servidores de Comando e Controle (C2).
- [ ] D) Um relatório descrevendo o impacto legal de um vazamento de dados.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> IoCs são evidências forenses tangíveis e técnicas (Hashes de malware, IPs maliciosos, URLs suspeitas, chaves de registro alteradas) que você pode inserir imediatamente no SIEM para procurar pela ameaça na sua rede.
</details>
<br>

**14. Uma empresa financeira prioriza a integridade das transações acima de qualquer coisa. Durante um ataque ao servidor SQL, o analista Tier 2 decide desligar completamente o servidor da tomada para evitar alteração nos saldos dos clientes. Qual foi o trade-off (troca) de segurança feito nesta ação?**
- [ ] A) Ele sacrificou a Confidencialidade para manter a Integridade.
- [ ] B) Ele sacrificou a Disponibilidade (Availability) para garantir a Integridade.
- [ ] C) Ele sacrificou a Autenticação para manter a Disponibilidade.
- [ ] D) Não houve sacrifício, ele aplicou a Defesa em Profundidade.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Ao desligar o servidor, ninguém mais consegue acessar o sistema (quebra da Disponibilidade/Availability). No entanto, isso garante que os dados dos saldos não sofrerão adulteração maliciosa (garantia da Integridade).
</details>
<br>

**15. Qual é o papel de uma plataforma TIP (Threat Intelligence Platform) integrada ao SOC?**
- [ ] A) Bloquear o tráfego não autorizado na borda da rede.
- [ ] B) Fazer backup automático de dados críticos.
- [ ] C) Centralizar, agregar e classificar feeds de inteligência de ameaças externas (como feeds de IoCs pagos ou open-source) para enriquecer os alertas do SIEM.
- [ ] D) Controlar o acesso físico aos servidores do data center.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C</b><br>
<i>Explicação:</i> Uma TIP coleta "Threat Feeds" do mundo todo (ex: AlienVault OTX, VirusTotal, Cisco Talos) e alimenta o SIEM. Assim, se um IP que acabou de ser classificado como malicioso na Europa tentar acessar sua rede no Brasil, seu SIEM já saberá bloqueá-lo.
</details>
