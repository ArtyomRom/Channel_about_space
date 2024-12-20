# Скрипт для публикации фотографий космической тематики в телеграмм канал
- Позволят скачивать фотографии и публиковать посты по космической тематики

## Как установить


  - ***Операционная система:***  
    - Windows 10 или новее
    - macOS 10.14 или новее
    - Linux (разные дистрибутивы)

  - ***Язык программирования:***  
    - Python 3.6 или новее


  ## Установка окружения

  1. Склонируйте репозиторий:
   [link](https://github.com/ArtyomRom/Channel_about_space.git)

  2. Создайте виртуальное окружение:
        ```bash
        python -m venv venv
        ```

  3. Активируйте виртуальное окружение:
   
    - На Windows:
      ```bash
      venv\Scripts\activate
      ```
    - На macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

  4. Установите зависимости:
    ```bash
       pip install -r requirements.txt
    ```
  5. Получить токен для скачивания картинок можно на сайте https://api.nasa.gov
     
     Заполнив форму:
     ![img.png](img.png)
  
  6. Получить токен для телеграмм-бота с канала @BotFather
  7. Создать телеграмм группу и поставить телеграмм-бота администратором 
  8. Переменные окружения
  - NASA_API_KEY - ключ API для скачивание фотографий
  - TG_BOT_API - ключ API телеграмм-бота
  - link_tg_channel - ссылка на группу телеграмм, куда будут публиковаться посты
  9. Запуск для скачивания фотографий:
     - Пример
       ```bash
          python main.py --launch=1
       ```
       ![img_1.png](example.png)
     В качестве параметров можно передать откуда вы хотите получить фотографии
       - launch фотографии с запуска SpaceX.
       - nasa - фотографии с сайта Nasa
       - earth - фотографии земли
       - launch_id - если указать будут скачены фотографии конкретного старта, в противном случае с последннего старта
  10. Запуск для публикации постов:     
      - Пример
       ```bash
          python public_post.py --time_public=2
       ```
       ![img_1.png](example_2.png)

## Цель проекта
  - Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.

## Примеры поста в телеграмм группе:
  ![img_1.png](img_1.png)

 