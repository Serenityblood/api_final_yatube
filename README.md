# api final

## Что это за проект?

> Это API для проекта Yatube, позволяющая получать, удалять, редактировать
> данные о постах и пользователях посредством запросов через API
> Все данные возвращаются в формате JSON 

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Serenityblood/api_final_yatube.git
cd api_final_yatube
```

### Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

### Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

### Выполнить миграции:

```
python3 manage.py migrate
```

### Запустить проект:

```
python3 manage.py runserver
```

## Документация:
> Находится на эндпоинте: http://127.0.0.1:8000/redoc/

## Примеры ответов API:

> GET запрос на эндпоинт: api/v1/posts/?limit=1&offset=0
> Ответ:
```
{
    "count": 3,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=1&offset=1",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "blood",
            "text": "exampe text",
            "pub_date": "2022-09-14T10:22:52.257596Z",
            "image": null,
            "group": null
        }
    ]
}
```
> GET запрос на эндпоинт: api/v1/posts/{post_id}/comments/
> Ответ:
```
[
    {
        "id": 1,
        "author": "blood",
        "post": 1,
        "text": "exampe comment text 1",
        "created": "2022-09-14T10:37:32.837715Z"
    },
    {
        "id": 2,
        "author": "blood",
        "post": 1,
        "text": "exampe comment text 2",
        "created": "2022-09-14T10:39:48.366073Z"
    }
]
```