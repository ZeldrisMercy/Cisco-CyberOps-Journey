# 🛡️ LEVEL 4: THE LINUX TERMINAL (KALI & CYBEROPS ESSENTIALS)

![CISCO](https://img.shields.io/badge/CISCO-NETACAD-orange) ![STATUS](https://img.shields.io/badge/IN%20PROGRESS-yellow) ![FOCUS](https://img.shields.io/badge/FOCUS-BLUE%20TEAM-blue)

## 📊 PROGRESSO DA MISSÃO

* **Módulo 4.1: Linux Basics** — Status: 100% Concluído
* **Módulo 4.2: Working in the Linux Shell** — Status: Em Andamento
* **Módulo 4.3: Linux Administration** — Status: Bloqueado (Aguardando Nível)

---

## ⚔️ SKILL TREE (HABILIDADES DESBLOQUEADAS)

### 4.1. FUNDAMENTOS DO SISTEMA E SOC (THE CORE)
* **Linux no SOC:** Entendimento da importância do Linux como espinha dorsal da cibersegurança e operações de Blue Team.
* **Estrutura de Código Aberto:** Compreensão do valor do Linux e sua flexibilidade para ferramentas de segurança.

### 4.2. COMANDOS BÁSICOS E OPERAÇÕES DE SHELL
* **Navegação e Manipulação:** Domínio de comandos fundamentais para gestão de arquivos e diretórios.
* **Acesso Interativo (Root):** Uso do `sudo -i` para carregar variáveis de ambiente e perfil do superusuário, garantindo controle total do sistema.
* **Data Duplicator (dd):** Definição técnica do `dd` para cópia e conversão de dados bit a bit, essencial para clonagem de discos e imagens forenses.

### 🔍 BUSCA E FILTRAGEM (SEARCH SKILLS)
* **The Power of Grep:** Uso do `grep` (Global Regular Expression Print) para localizar strings específicas dentro de arquivos ou saídas de outros comandos.
* **Piping & Redirection:** Mecânica de conectar comandos onde o `grep` é colocado ao final da linha via pipe (`|`) para filtrar resultados.
* **Monitoramento de Processos:** Uso do `ps` (Process Status) para capturar o estado dos processos e filtrar alvos específicos.

---

## 🏆 ESTRATÉGIAS DE CTF & AUDITORIA

| Técnica | Comando | Objetivo Cibersegurança |
| :--- | :--- | :--- |
| **Flag Hunting** | `ls /alvo \| grep "xxx"` | Localizar arquivos de desafio que seguem um padrão de nomenclatura. |
| **Deep Search** | `grep -r "xxx" .` | Busca recursiva de tokens ou flags dentro do conteúdo de múltiplos arquivos. |
| **Log Analysis** | `cat /var/log/auth.log \| grep "failed"` | Identificar tentativas de intrusão e falhas de autenticação em logs. |
| **Process Hunt** | `ps aux \| grep [p]rocesso` | Localizar PIDs de processos específicos sem exibir o próprio comando grep. |

---

## 🧪 LABS PRÁTICOS (FIELD REPORTS)

* **LAB 4.2.7 - Getting Familiar with the Linux Shell:** Prática inicial de comandos CLI e exploração da estrutura de diretórios.
* **LAB 4.2.6 - Working with Text Files in the CLI:** Exercícios focados na criação, edição e manipulação de arquivos de texto via terminal.

---

### 🛠️ Toolset Aplicado
* Bash (Linux Shell)
* Grep (Pattern Matcher)
* System Utilities (ps, dd, ls)
* Sudo (Privilege Management)

---

*Documentação mantida por **Ícaro de Souza Mariano** | Especialista em Formação**
