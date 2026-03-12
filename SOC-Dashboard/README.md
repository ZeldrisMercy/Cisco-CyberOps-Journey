# 🌐 Web-SOC-Dashboard: Visualização de Incidentes

Este diretório contém a camada de visualização do ecossistema SOC. Trata-se de uma interface **SIEM (Security Information and Event Management)** leve, projetada para fornecer consciência situacional ao analista em tempo real.

## 🖼️ Funcionalidades
* **Live Feed de Eventos:** Exibe os logs de ataques conforme chegam à API Java, com destaque visual para IPs bloqueados (`[BLOQUEADO_VIA_INTEL]`).
* **Métricas de Risco:** Gráfico dinâmico (Chart.js) que compara o nível de periculosidade de cada IP detectado.
* **Geolocalização Visual:** Identificação de países de origem dos ataques nos logs de eventos.
* **Geração de Relatórios:** Módulo exportador que gera arquivos `.txt` de auditoria contendo todos os incidentes registrados no banco de dados, facilitando a documentação de incidentes (IR).

## 🛠️ Tecnologias Utilizadas
* **Frontend:** HTML5, CSS3 (Modern Dark Theme).
* **Charts:** [Chart.js](https://www.chart.js.org/).
* **Data Flow:** Fetch API (comunicação assíncrona com o Backend Java).
* **Refresh Rate:** Atualização automática a cada 5 segundos via `setInterval`.

## 🚀 Como Utilizar
1. Certifique-se de que o **Java-Sec-API** está rodando na porta `8080`.
2. Abra o arquivo `index.html` em qualquer navegador moderno.
3. Monitore os ataques em tempo real e utilize o botão **"Gerar Relatório de Incidentes"** para exportar os logs.

## 📁 Estrutura
* `index.html`: Arquivo central contendo a interface, estilização e a lógica JavaScript para consumo da API REST.
