# locust-load-test-mock
Um mock para quando necessitar realizar um teste de carga em uma api

- Instalação: poetry install
- Execução: poetry run locust --host=http://localhost:8000 
- Execução headless: poetry run locust --host=http://localhost:8000 --users 100 --spawn-rate 2 --headless
