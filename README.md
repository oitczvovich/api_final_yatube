Польза проекта в том, что он дает пользоваться функционалом приложения не посещая сайт.
Реализован функционал дающий возможность:

    Просматривать, создавать новые, удалять и изменять посты.
    Просматривать и создавать группы.
    Комментировать, смотреть, удалять и обновлять комментарии.

Установка

Клонируем репозиторий на локальную машину:

$ git clone https://github.com/oitczvovich/api_yatube.git

Создаем виртуальное окружение:

$ python -m venv venv

Устанавливаем зависимости:

$ pip install -r requirements.txt

Создание и применение миграций:

$ python manage.py makemigrations и $ python manage.py migrate

Запускаем django сервер:

$ python manage.py runserver

Примеры запросов и ответов. 
Для запросов используется Rest Client для VSC:

api/v1/api-token-auth/ (POST): передаём <username> и <password>, получаем токен.
    Запрос:

    POST  http://127.0.0.1:8000/api/v1/api-token-auth/
    Content-Type: application/json
    {
        "username": "<username>",
        "password": "<password>"
    }
    Ответ:

    {
    "token": "g45g645635g6y54y3f67rf5g75656f7ty563gh"
    }
    Полученный токен необходимо указаывать в дальнейших запросах в поле Authorization: 

api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
    (GET) запорос возможен от не автороизованного пользователя.
    Запрос:

    POST  http://127.0.0.1:8000/api/v1/posts/
    Content-Type: application/json
    Authorization: Token g45g645635g6y54y3f67rf5g75656f7ty563gh # указать токен     который получили ранее.

    {
        "text": "Первый пост",
        "group": 1 # не обязательное поле
    }

    Ответ: 

    {
        "id": 24,
        "author": "pomoradmin",
        "text": "Первый пост",
        "pub_date": "2022-06-01T08:23:09.065853Z",
        "image": null,
        "group": 1
    }

api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
api/v1/groups/ (GET): получаем список всех групп.
api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.