# Загрузка фотографий в Telegram

Набор скриптов загружает фотографии космической тематики в Telegram канал.

## Как установить

### Окружение
Python должен быть установлен.

### Зависимости
Используйте pip для установки зависимостей :
```bash
pip install -r requirements.txt
```
### Переменные окружения

Отредактируйте `.env` для необходимых настроек.
Пример `.env.example`:
```
NASA_API_KEY={Your NASA API Key}
TELEGRAM_TOKEN={Your Telegram Token}
TELEGRAM_CHANNEL={Your Telegram channel id}
PUBLISH_DELAY=10
```
### fetch_spacex.py
Загружает с сайта компании [SpaceX](https://api.spacexdata.com) информацию о запусках. Фотографии запуска сохраняет в директорию `images\spacex`. Запуск:
```bash 
$ python fetch_spacex.py
```

### fetch_nasa.py
Загружает с сайта компании космического агенства [NASA](https://api.nasa.gov/) фотографии в директорию `images\nasa`. Для доступа к фотографиям необходимо сгенерировать API Key [NASA](https://api.nasa.gov/#signUp), сохранить в `NASA_API_KEY` файла `.env`. Запуск:
```bash 
$ python fetch_nasa.py
```

### to_telegram.py
Публикует загруженные фотографии в Telegram канал, настройка `TELEGRAM_CHANNEL` в файле `.env`. Ваш Telegram Token необходимо сохранить в `TELEGRAM_TOKEN` файла `.env`. Периодичность публикации составляет 24 часа. Периодичность можно задать в `PUBLISH_DELAY=10` (секунды) файла `.env`. Запуск:
```bash 
$ python to_telegram.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
