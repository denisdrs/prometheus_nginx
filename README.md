# Documentação do Projeto: Monitoramento com Prometheus e Grafana

Este projeto implementa uma arquitetura de monitoramento usando  **Prometheus**, **Grafana** e o **Nginx Prometheus Exporter**. O objetivo é coletar e visualizar métricas do servidor Nginx, como quantidade de usuários ativos e número de requisições. Aqui estão os detalhes dos endpoints e como eles interagem dentro da arquitetura.

## Endpoints e Funções

### 1. **Nginx** (`http://localhost:8080`)
- **Função**: Servir uma página HTML (definida pelo arquivo `index.html`) e expor métricas via `/stub_status`.
- **Endpoint Principal**:
  - `http://localhost:80`: Página principal, exibindo o conteúdo do `index.html`.
  - `http://localhost:80/stub_status`: Exposição das métricas nativas do Nginx, como:
    - Conexões ativas
    - Total de requisições processadas
    - Conexões em estados específicos (aceitas, aguardando, etc.)
- **Relação**: Este serviço é o núcleo da aplicação, sendo monitorado diretamente pelo **Nginx Prometheus Exporter**.

### 2. **Nginx Prometheus Exporter** (`http://localhost:9113`)
- **Função**: Exportar as métricas do Nginx para o Prometheus em formato compatível.
- **Endpoint Principal**:
  - `http://localhost:9113/metrics`: Exposição das métricas coletadas do endpoint `/stub_status` do Nginx.
    - Exemplo de métricas exportadas:
      - `nginx_connections_active`: Número de conexões ativas.
      - `nginx_http_requests_total`: Total de requisições processadas.
      - `nginx_connections_accepted`: Total de conexões aceitas.
- **Relação**: Este serviço atua como um intermediário, transformando as métricas do Nginx em um formato que o Prometheus possa coletar e armazenar.

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
- **Relação**: É a camada de apresentação que permite visualizar e interpretar as métricas coletadas pelo Prometheus.

## Fluxo de Dados
1. O **Nginx** expõe métricas nativas via o endpoint `/stub_status`.
2. O **Nginx Prometheus Exporter** coleta essas métricas e as transforma em um formato compatível com o **Prometheus**.
3. O **Prometheus** coleta e armazena as métricas do Exporter.
4. O **Grafana** consulta o **Prometheus** e apresenta as métricas em dashboards interativos.

## Arquitetura Resumida
- **Nginx**: Servidor web e fonte das métricas.
- **Nginx Prometheus Exporter**: Transforma as métricas do Nginx para Prometheus.
- **Prometheus**: Centraliza as métricas e fornece dados para o Grafana.
- **Grafana**: Visualiza e analisa as métricas.

## Configuração
1. Certifique-se de ter todos os arquivos necessários:
   - `Dockerfile`: Configura a imagem do Nginx.
   - `nginx.conf`: Configuração personalizada do Nginx.
   - `page.html`: Página servida pelo Nginx.
   - `prometheus.yml`: Configuração do Prometheus para monitorar o Exporter.
   - `docker-compose.yml`: Orquestra todos os serviços.

2. Inicie os serviços com:
   ```bash
   docker-compose up -d
   ```

3. Acesse os endpoints nas seguintes URLs:
   - Nginx: [http://localhost:8080](http://localhost:8080)
   - Prometheus: [http://localhost:9090](http://localhost:9090)
   - Grafana: [http://localhost:3000](http://localhost:3000)




- Configure alertas no Prometheus para monitorar situações críticas, como aumento inesperado no número de conexões.

---

Este projeto fornece uma arquitetura básica de monitoramento para aplicações baseadas em Nginx. Sinta-se à vontade para expandir a solução, adicionando
