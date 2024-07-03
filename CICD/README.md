### CI/CD
Для развертывания контейнера используются команды:
```
docker build -t server .
docker run -d -p 8000:8000 server
```
или в одну команду через **docker-compose**:
```
docker-compose up -d
```
Проверка работы сервера возможна с помощью команды:
```
curl -X GET http://127.0.0.1:8000/healthz
```
