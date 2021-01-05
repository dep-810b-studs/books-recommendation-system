# Приложение доступно по адресу 
<br/> http://shvasily.pythonanywhere.com/

# Инструкция по запуску
## Запуск в режиме demon(без логов)
`docker-compose -f ./docker-compose.yaml up -d --build`
## Запуск с выводом логов в консоль
`docker-compose -f ./docker-compose.yaml up --build`
<br/> Приложение будет доступно по адресу http://localhost:8000
## Локальный запуск
`pip install -r requirements.txt`
 <br/>`python ./manage.py runserver 8000`