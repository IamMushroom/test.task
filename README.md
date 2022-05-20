# Тестовое задание

Привет =)  
Это небольлая задачка: web-приложение, пишущее "Hello, World!", Dockerfile для его контейнеризации и docker-compose.yml для резвертывания приложения и окружения (Prometheus и Grafana)  
  
## Структура
1. В папке src лежит приложение на Python 3.10 и скрипт для проверки здоровья.
2. В папке prom_config лежит yml Prometheus с настройками для получания метрик от приложения
3. В папке graf_config/provisioning лежат:
    + В папке datasources – yml для подключения к Prometheus
    + В папке dashboards – yml и json для импорта дашбордов

## src

### vars.py
Список глобальных переменных.
### hello.py
Само приложение.  
Поднимает на порте vars.external_port веб-сервер, и выводит сообщение vars.http_message.  
Из модуля prometheus-client импортируются функция start_http_server и классы Counter и Summary. Формируются две метрики: REQUESTS – количество запросов к серверу и LATENCY – время, потраченное сервером на обработку запроса.  
Метрики доступны по порту vars.prometheus_port.
### healthcheck.py
Определил функцию, в которую передаю url, а на выходе получаю True, если получил код 1XX, 2XX или 3XX, и False, если код 4XX, 5XX или url не отвечает. Также, полученный код пишу в файл health.log.  
После этого, передаю в функцию url приложения, и, если проверка прошла – выхожу с кодом 0, иначе – с кодом 1.

## prom_conf
### prometheus.yml
Файл с настройками узла и интервалами опроса.

## graf_conf/provisioning
### datasources/prom.yml
Файл с настройками подключения к Prometheus.
### dashboards/dashboards.yml
Файл с настройками дашбордов.
### dashboards/hello-app.json
Описание дашборда. Был получен экспортом из графаны.   
Выводит мои метрики (латенси и кол-во запросов), и память, занимаемую приложением.

## .env
Содержит переменные для docker-compose.yml.

## docker-compose.yml
Запускаем три сервиса:
1. Приложение hello.
2. Когда статус приложения hello станет healthy, запускаем Prometheus. Через wget проверяем, что сервис доступен.
3. Когда статус Prometheus станет healthy, запускаем Grafana. Через wget проверяем, что сервис доступен. Отключаем возможность регистрироваться, и устанавливаем пароль от админа

## Dockerfile
Используем образ python:3.10-alpine3.15.  
Копируем содержимое папки src и файл requirements.txt в контейнер.  
Отключаем буферизацию.  
Обновляем pip и устанавливаем модули из файла requirements.txt.  
Открываем порты 8000 и 8001.  
Настраиваем healthcheck.  
Создаём папку для лога проверки здоровья и запускаем приложение.  

## requirements.txt
Файл содержит дополнительные зависимости для приложения hello.

# Как запустить?
В файле docekr-compose.yml прописан уже собранный образ приложения, загруженный в мой репозиторий, так что достаточно запустить:  
``` bash
git clone https://gitlab.com/iammushroom/test.task
docker compose up -d --build
```
