# Monitoramento com Prometheus e Grafana

Este projeto implementa uma arquitetura de monitoramento usando  **Prometheus**, **Grafana** e o **Nginx Prometheus Exporter**. O objetivo é coletar e visualizar métricas do servidor Nginx, como quantidade de usuários ativos e número de requisições.

## Endpoints e Funções

### 1. **Nginx** (`http://localhost:8080`)
- **Função**: Servir uma página HTML (definida pelo arquivo `index.html`) e expor métricas via `/stub_status`.
- **Endpoint Principal**:
  - `http://localhost:80`: Página principal, exibindo o conteúdo do `index.html`.
  - `http://localhost:80/stub_status`: Exposição das métricas nativas do Nginx, como:
    - Conexões ativas
    - Total de requisições processadas
    - Conexões em estados específicos (aceitas, aguardando, etc.)
- **Obs**: Este serviço é o núcleo da aplicação, sendo monitorado diretamente pelo **Nginx Prometheus Exporter**.

### 2. **Nginx Prometheus Exporter** (`http://localhost:9113`)
- **Função**: Exportar as métricas do Nginx para o Prometheus em formato compatível.
- **Endpoint Principal**:
  - `http://localhost:9113/metrics`: Exposição das métricas coletadas do endpoint `/stub_status` do Nginx.
    - Exemplo de métricas exportadas:
      - `nginx_connections_active`: Número de conexões ativas.
      - `nginx_http_requests_total`: Total de requisições processadas.
      - `nginx_connections_accepted`: Total de conexões aceitas.
- **Obs**: Este serviço atua como um intermediário, transformando as métricas do Nginx em um formato que o Prometheus possa coletar e armazenar.

### 3. **Prometheus** (`http://localhost:9090`)
- **Função**: Coletar e armazenar as métricas de diversos serviços, incluindo o **Nginx Prometheus Exporter**.
- **Endpoint Principal**:
  - `http://localhost:9090`: Interface web para consultas às métricas e gestão de configurações do Prometheus.
  - **Scrape Target**:
    - `http://nginx-exporter:9113/metrics`: O Prometheus coleta métricas deste endpoint periodicamente.
- **Relação**: Centraliza as métricas e fornece uma base para visualizações e alertas no Grafana.

### 4. **Grafana** (`http://localhost:3000`)
- **Função**: Visualizar e analisar as métricas coletadas pelo Prometheus.
- **Endpoint Principal**:
  - `http://localhost:3000`: Interface web para criação de dashboards e consulta de métricas.
- **Configuração**:
  - Configurado para se conectar ao Prometheus como fonte de dados.
  - Dashboards personalizados podem ser criados para exibir métricas do Nginx, como conexões ativas e número de requisições por segundo.
- **Obs**: É a camada de apresentação que permite visualizar e interpretar as métricas coletadas pelo Prometheus.

## Fluxo de Dados
![Descrição do GIF](https://media.giphy.com/media/7F7bjODRXzGj3UptzQ/giphy.gif)
1. O **Nginx** expõe métricas nativas via o endpoint `/stub_status`.
2. O **Nginx Prometheus Exporter** coleta essas métricas e as transforma em um formato compatível com o **Prometheus**.
3. O **Prometheus** coleta e armazena as métricas do Exporter.
4. O **Grafana** consulta o **Prometheus** e apresenta as métricas em dashboards interativos.

## Arquitetura Resumida
- **Nginx**: Servidor web e fonte das métricas.
- **Nginx Prometheus Exporter**: Transforma as métricas do Nginx para Prometheus.
- **Prometheus**: Centraliza as métricas e fornece dados para o Grafana.
- **Grafana**: Visualiza e analisa as métricas.


## Acesse os endpoints nas seguintes URLs:
   - Nginx: [http://localhost:8080](http://localhost:8080)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - Grafana: [http://localhost:3000](http://localhost:3000)
   - Exporter: [http://localhost:9113/metrics](http://localhost:9113/metrics)




- Objetivo: Monitorar situações críticas, como aumento inesperado no número de conexões.

---

Projeto simples com foco em apredizado de uma arquitetura basica do Prometheus.
## Autores

- [@denisdrs](https://www.github.com/denisdrs)
