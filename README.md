## Описание проекта

#Как запустить проект:

Клонировать репозиторий

`git@github.com:Dragonwlad/api_final_yatube.git`

 Перейти в него 
 
`cd api_final_yatube`

Cоздать и активировать виртуальное окружение:
`python -m venv venv`
`source venv/bin/activate`

Установить зависимости из файла requirements.txt:
`pip install -r requirements.txt`

Перейти в папку с файлом **manage.py** :
`cd yatube_api/`

Выполнить миграции:
`python manage.py migrate`


## Как запустить проект
Запустить проект:
`python manage.py runserver`

## Документация по проекту
`http://127.0.0.1:8000/redoc/`

## Примеры
# Создать пользователя в терминале:
`python manage.py createsuperuser`
# Дополнительно пользователей можно создать через панель администратора, войдя под супер пользователем:
`http://127.0.0.1:8000/admin`
(адрес *127.0.0.1:8000* может отличаться от вашего, см. в консоль)

# Получить список всех публикаций
http://127.0.0.1:8000/api/v1/posts/

# Добавление новой публикации в коллекцию публикаций
http://127.0.0.1:8000/api/v1/posts/

Пример вложения:
*{
"text": "string",
"image": "string",
"group": 0
}*

Пример ответа:
*{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}*
