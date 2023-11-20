from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from flask import Response

app = Flask(__name__)

# Definindo uma métrica de contador para contagem de requisições
ping_counter = Counter('ping_request_count', 'Number of requests handled by Ping handler')

# Rota para o endpoint /ping
@app.route('/ping')
def ping():
    # Incrementa o contador de requisições
    ping_counter.inc()
    return 'pong'

# Rota para o endpoint /metrics, que expõe métricas para o Prometheus
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8091)

