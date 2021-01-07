# Инструкция по запуску
#### Перед запуском необходимо скачать дамп объекта рекомендательной системы
`./download_dump.sh`
<br/> Либо по ссылке https://drive.google.com/file/d/1SIgr1ULQR3rRNfVOBiyhKvjkEkwYaoku/view?usp=sharing
<br/> В итоге дамп должен лежать в корне проекта (в одном каталоге с файлом manage.py)
## Запуск в режиме demon(без логов)
`docker-compose -f ./docker-compose.yml up -d --build`
## Запуск с выводом логов в консоль
`docker-compose -f ./docker-compose.yml up --build`
<br/> Приложение будет доступно по адресу http://localhost:8000
## Локальный запуск
`pip install -r requirements.txt`
 <br/>`python ./manage.py runserver 8000`
## Приложение доступно по адресу 
<br/> http://shvasily.pythonanywhere.com/
<br/> P.S.: В приложении, развернутом на pythonanywhere используется stub режим рекомендательной системы из-за ограничений по ПЗУ.
