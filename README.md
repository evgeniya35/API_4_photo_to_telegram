# Загрузка фотографий в Telegram

Набор скриптов загружает фотографию в Telegram

## Окружение

Python должен быть установлен.

### Зависимости

Используйте pip для установки зависимостей:
```bash
pip install -r requirements.txt
```

### Переменные окружения

Отредактируйте `.env` для необходимых настроек:
...
[//]: # (

* `DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME` настройка подключения к БД.
* `ALLOWED_HOSTS=127.0.0.1,localhost` cписок хостов/доменов, для которых может работать текущий сайт.
Пример `.env.example`:
```
SECRET_KEY=REPLACE_ME
DB_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
DEBUG=False
ALLOWED_HOSTS=127.0.0.1,localhost
```

#### Запуск

Запустите Python:
```bash
$ python manage.py runserver 0.0.0.0:8000
```

#### Как работает

* Откройте приложение в браузере. [По умолчанию http://127.0.0.1:8000/](http://127.0.0.1:8000/) 

![](images/app.png)

## Особенности работы
)
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
