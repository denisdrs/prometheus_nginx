# Exemplo em Python com prometheus_client
from prometheus_client import start_http_server, Counter

REQUEST_COUNT = Counter('app_requests_total', 'Total Requests')

if __name__ == '__main__':
    start_http_server(8000)  # Porta onde o Prometheus buscará as métricas
    while True:
        REQUEST_COUNT.inc()  # Incrementa o contador
