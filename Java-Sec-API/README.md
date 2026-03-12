# ☕ Java Sec API (Spring Boot Gateway)

> **Missão:** Isolar o banco de dados e aplicar regras de negócio. Esta API RESTful atua como o *Gateway* central do nosso SOC, intermediando a comunicação entre os scripts de detecção (Python) e o armazenamento de longo prazo (SQL).

Construída em **Java 17+** com o ecossistema **Spring Boot**, esta API demonstra a aplicação de arquitetura corporativa para ferramentas de segurança, garantindo que nenhum script na borda da rede tenha acesso direto às credenciais do banco de dados relacional.

---

## 🏗️ Arquitetura MVC & Endpoints

O tráfego de dados obedece ao padrão Controller -> Service -> Repository:

* **`POST /api/v1/threats`**: Recebe alertas em formato JSON dos agentes Python (`soc_ips_blocker.py`) quando um IP é bloqueado e registra no banco.
* **`GET /api/v1/threats/top`**: Retorna os IPs mais perigosos para alimentar o futuro Dashboard Web.
* **`GET /api/v1/quiz/modules`**: Disponibiliza os módulos de estudo do banco de dados para a interface do simulador.

---

## ⚙️ Stack Tecnológico
* **Linguagem:** Java 17 (Tipagem forte e Orientação a Objetos)
* **Framework:** Spring Boot 3 (Web, Data JPA)
* **Persistência:** Hibernate (ORM) integrado ao SQLite
* **Build Tool:** Maven

---
*Desenvolvido e mantido por **Ícaro de Souza Mariano** | Conecte-se comigo no [LinkedIn](http://www.linkedin.com/in/icaro-s-m).*
