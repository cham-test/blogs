Для запуска проекта выполнить: docker-compose up --build  <br>
Для создания суперпользователя: docker exec -it blogs_app_1 python manage.py createsuperuser <br>
Если скажет что такого контейнера нет его имя можно легко найти при выводе команды docker ps | grep blogs_app <br>
Для корректной работы почты и csrf_middleware нужно создать файл credentials.py в директории app/blogs/ <br>
с заполнеными значениями переменных: <br> 
SECRET_KEY  <br>
EMAIL_HOST <br>
EMAIL_HOST_USER <br>
EMAIL_HOST_PASSWORD  <br>
EMAIL_PORT <br>
EMAIL_USE_TLS <br>
