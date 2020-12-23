Для запуска проекта выполнить: docker-compose up --build  <br>
Для создания суперпользователя: docker exec -it blogs_app_1 python manage.py createsuperuser <br>
Если скажет что такого контейнера нет его имя можно легко найти при выводе команды docker ps | grep blogs_app
