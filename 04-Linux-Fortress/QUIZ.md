# 🧠 Simulado Definitivo: Module 04 (Linux Fortress)

Estas 18 questões cobrem a fundo a administração do sistema, matemática de permissões, análise de rede via CLI e investigação de logs, desenhadas no estilo de cenário técnico do exame **Cisco CBROPS 200-201**.

---

### 📁 Domínio 1: Sistema de Arquivos e Permissões

**1. Um analista de SOC precisa tornar um script bash (`triage.sh`) executável apenas para o criador do arquivo. O grupo e os outros usuários só devem ter permissão de leitura. Qual comando aplica essa configuração exata?**
- [ ] A) `chmod 777 triage.sh`
- [ ] B) `chmod 744 triage.sh`
- [ ] C) `chmod 644 triage.sh`
- [ ] D) `chmod 755 triage.sh`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (`chmod 744`)</b><br>
<i>Explicação:</i> 7 (4 Leitura + 2 Gravação + 1 Execução) para o Dono. 4 (Apenas Leitura) para o Grupo. 4 (Apenas Leitura) para Outros. O 644 daria leitura e gravação ao dono, mas não execução.
</details>
<br>

**2. Durante a resposta a um incidente, você descobre um binário malicioso dentro de um diretório. Qual é a localização clássica e perigosa no Linux que, por padrão, permite que qualquer usuário do sistema crie e grave arquivos nela, sendo frequentemente usada como "ponto de pouso" para malwares?**
- [ ] A) `/etc`
- [ ] B) `/var/log`
- [ ] C) `/sbin`
- [ ] D) `/tmp`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D (`/tmp`)</b><br>
<i>Explicação:</i> O diretório de arquivos temporários `/tmp` tem permissões amplas (geralmente 1777, com sticky bit) para que qualquer programa ou usuário possa gravar lá. É o local favorito para atacantes baixarem seus scripts de exploração iniciais.
</details>
<br>

**3. Um atacante excluiu o arquivo de log `/var/log/auth.log` para esconder seus rastros. No entanto, o administrador havia criado previamente um "Hard Link" (link físico) desse arquivo em uma pasta secreta. O que acontece com os dados do log?**
- [ ] A) Os dados são perdidos, e o Hard Link se torna um atalho quebrado.
- [ ] B) Os dados ainda existem e podem ser lidos através do Hard Link, pois ele aponta diretamente para o Inode no disco.
- [ ] C) O sistema operacional impede a exclusão do arquivo original se um Hard Link existir.
- [ ] D) Os dados são movidos para a lixeira (`/dev/null`).

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> Diferente do Soft Link (que é só um atalho), o Hard Link é um ponteiro direto para o bloco de dados físico (Inode). Mesmo apagando o arquivo original, os dados continuam no disco e acessíveis enquanto houver pelo menos um Hard Link apontando para eles.
</details>

---

### 💻 Domínio 2: Navegação, Arquivos e Redirecionamento

**4. Você está criando um script para salvar o resultado de uma auditoria em um arquivo de texto existente chamado `auditoria.txt`. Qual operador você deve usar para garantir que os dados novos sejam adicionados ao final do arquivo, sem apagar (sobrescrever) o histórico que já estava lá?**
- [ ] A) `>`
- [ ] B) `>>`
- [ ] C) `<`
- [ ] D) `|` (Pipe)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (`>>`)</b><br>
<i>Explicação:</i> O operador `>>` (Append) adiciona a saída ao final do arquivo existente. O operador `>` (Redirect) sobrescreve o arquivo inteiro, destruindo os dados anteriores.
</details>
<br>

**5. Qual arquivo oculto (dot-file), localizado no diretório `/home` do usuário, é frequentemente modificado por atacantes para criar persistência, alterando a variável PATH ou criando aliases maliciosos que são executados toda vez que o usuário abre um terminal?**
- [ ] A) `/etc/shadow`
- [ ] B) `.bashrc` ou `.bash_profile`
- [ ] C) `resolv.conf`
- [ ] D) `/etc/passwd`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (`.bashrc`)</b><br>
<i>Explicação:</i> O `.bashrc` é executado automaticamente sempre que o usuário inicia uma sessão de shell. Atacantes inserem comandos aqui para garantir que seus malwares voltem a rodar assim que a vítima abrir o terminal.
</details>
<br>

**6. Se um analista quiser visualizar apenas as últimas 15 linhas de um arquivo de log que está sendo atualizado rapidamente, e quiser que a tela continue mostrando novas entradas em tempo real, qual comando ele deve usar?**
- [ ] A) `cat arquivo.log`
- [ ] B) `grep arquivo.log`
- [ ] C) `tail -f arquivo.log`
- [ ] D) `head -n 15 arquivo.log`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (`tail -f`)</b><br>
<i>Explicação:</i> O comando `tail` mostra o final do arquivo, e a flag `-f` (follow) mantém o arquivo aberto, imprimindo as novas linhas na tela no exato momento em que elas são escritas pelo sistema.
</details>

---

### 🕵️ Domínio 3: Processos e Investigação de Rede

**7. Você suspeita que o servidor está rodando um serviço de C2 (Comando e Controle). Qual comando fornecerá uma lista de todas as conexões TCP e UDP, não resolverá os nomes de domínio (para ser mais rápido) e mostrará o Process ID (PID) responsável pela conexão?**
- [ ] A) `netstat -tunap`
- [ ] B) `ps -ejH`
- [ ] C) `nmap -sV 127.0.0.1`
- [ ] D) `tcpdump -i eth0`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: A (`netstat -tunap`)</b><br>
<i>Explicação:</i> `-t` (TCP), `-u` (UDP), `-n` (Numeric, não resolve nomes para não travar no DNS), `-a` (All sockets), `-p` (Mostra o PID e o nome do Programa).
</details>
<br>

**8. Ao analisar a árvore de processos no Linux usando `ps -ejH`, um conceito importante é o "Forking". O que isso significa no contexto de daemons de rede, como o servidor web Nginx ou Apache?**
- [ ] A) O processo principal divide a memória RAM em duas partes para evitar travamentos.
- [ ] B) O processo "Pai" cria cópias exatas de si mesmo (processos "Filhos") para que possam atender a múltiplas requisições de clientes simultaneamente.
- [ ] C) É a técnica onde o processo altera suas permissões de User para Root.
- [ ] D) O processo escreve seu conteúdo no disco de swap.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B**<br>
<i>Explicação:</i> Forking é o método padrão de concorrência em sistemas Unix. O processo mestre (root) faz um *fork* criando processos trabalhadores para lidar com conexões de rede simultâneas, melhorando a segurança e a performance.
</details>
<br>

**9. Você quer se conectar a um servidor na porta 22 (SSH) não para fazer login, mas para capturar a mensagem inicial que o servidor devolve, identificando assim a versão exata do software OpenSSH rodando lá. Como se chama essa técnica tática?**
- [ ] A) ARP Spoofing
- [ ] B) Packet Sniffing
- [ ] C) Banner Grabbing
- [ ] D) Port Forwarding

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Banner Grabbing)</b><br>
<i>Explicação:</i> Capturar o "banner" (a resposta em texto simples enviada por um daemon logo após o aperto de mãos da conexão TCP) é a forma mais rápida de descobrir qual serviço e qual versão estão escutando naquela porta.
</details>

---

### 📊 Domínio 4: Análise de Logs e Systemd

**10. Uma ferramenta automatizada tentou invadir o servidor SSH utilizando o usuário "root" com dezenas de senhas diferentes (Ataque de Força Bruta). Em qual arquivo de log do Ubuntu/Debian você encontraria a prova definitiva dessas tentativas falhas?**
- [ ] A) `/var/log/dmesg`
- [ ] B) `/var/log/auth.log`
- [ ] C) `/etc/shadow`
- [ ] D) `/var/log/messages`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (`/var/log/auth.log`)</b><br>
<i>Explicação:</i> O arquivo `auth.log` (ou `secure` no Red Hat/CentOS) registra todos os eventos relacionados à autorização e autenticação no sistema, incluindo su/sudo, logins SSH com sucesso e tentativas falhas.
</details>
<br>

**11. Qual comando substitui a análise manual de arquivos de texto de log em sistemas Linux modernos, permitindo consultar e filtrar eventos gerenciados diretamente pelo daemon `systemd`?**
- [ ] A) `chown`
- [ ] B) `journalctl`
- [ ] C) `lsblk`
- [ ] D) `ifconfig`

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (`journalctl`)</b><br>
<i>Explicação:</i> O utilitário `journalctl` consulta os logs coletados pelo `systemd-journald`. Ele permite filtros poderosos, como buscar logs de uma unidade de serviço específica (`journalctl -u nginx`) ou de desde o último boot (`-b`).
</details>
<br>

**12. O que o comando `mount /dev/sdb1 /mnt/analise_forense` faz no sistema operacional?**
- [ ] A) Copia os arquivos do disco sdb1 para a pasta analise_forense.
- [ ] B) Formata a partição física sdb1 para prepará-la para análise.
- [ ] C) Vincula a partição física de bloco (`/dev/sdb1`) a um diretório lógico (`/mnt/analise_forense`), tornando seus arquivos acessíveis aos usuários e programas.
- [ ] D) Criptografa o dispositivo utilizando os certificados encontrados na pasta.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: C (Montagem)</b><br>
<i>Explicação:</i> No Linux, dispositivos físicos de armazenamento não aparecem automaticamente como "Unidades". Eles precisam ser "montados" (mount) acoplando a estrutura do disco a um diretório existente (o Ponto de Montagem) na hierarquia `/`.
</details>

---

### 🛡️ Domínio 5: Ameaças Físicas e Serviços Essenciais

**13. Qual é a função de um "Rootkit" na arquitetura de um sistema Linux comprometido?**
- [ ] A) Criptografar a partição principal e exigir pagamento em Bitcoin.
- [ ] B) Alterar o código do Kernel ou de binários do sistema (como o próprio comando `ps` ou `netstat`) para ocultar a presença do atacante e de portas abertas na máquina.
- [ ] C) Realizar varreduras automáticas em outras redes em busca de vulnerabilidades.
- [ ] D) Destruir os setores de boot (MBR/GPT) para impedir a inicialização do sistema.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B (Ocultação via Rootkit)</b><br>
<i>Explicação:</i> Um Rootkit modifica as entranhas do sistema operacional. Se o atacante instalou um serviço malicioso e um rootkit, quando o analista digitar `ps -aux`, o comando `ps` (que foi infectado) mentirá, não mostrando o processo do atacante na lista.
</details>
<br>

**14. Por que o diretório `/etc` é de extrema importância para um analista que está conduzindo uma investigação de postura de segurança (Hardening)?**
- [ ] A) Porque é lá que os hashes das senhas de todos os usuários são armazenados (no arquivo passwd).
- [ ] B) Porque contém todos os arquivos de configuração (texto puro) que controlam o comportamento dos serviços e daemons do sistema (ex: onde o SSH escuta, regras de Firewall).
- [ ] C) Porque é o diretório padrão onde os backups de logs são rotacionados.
- [ ] D) Porque hospeda os executáveis compilados (binários) do sistema operacional.

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: B</b><br>
<i>Explicação:</i> O `/etc` é a central nervosa das configurações. Se um serviço está mal configurado e vulnerável, a correção ocorre alterando o arquivo `.conf` respectivo dentro deste diretório.
</details>
<br>

**15. Você tem um arquivo chamado `hashdump.txt` e quer enviá-lo de forma segura através de uma série de programas sem gravar em disco no meio do caminho. Qual caractere do Shell você usa para pegar a *Saída Padrão* (stdout) de um comando e conectá-la diretamente como *Entrada Padrão* (stdin) do próximo comando?**
- [ ] A) `&`
- [ ] B) `*`
- [ ] C) `>`
- [ ] D) `|` (Pipe)

<details>
<summary><b>✅ Ver Gabarito</b></summary>
<b>Resposta Correta: D (Pipe)</b><br>
<i>Explicação:</i> O Pipe (`|`) é o pilar da filosofia Linux. Exemplo: `cat auth.log | grep "Failed password" | awk '{print $11}'`. Ele passa os dados do comando da esquerda diretamente para processamento no comando da direita na memória RAM.
</details>
