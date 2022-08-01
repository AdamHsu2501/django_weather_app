# django_weather_app

1. Install Python <https://www.python.org/>
2. ****cmd****
    ```
    # install pipenv
    > pip install pipenv

    # download repo
    > git clone https://github.com/AdamHsu2501/django_weather_app.git        
    ```
3. Open broswer with https://home.openweathermap.org/ and create account. Then copy an api key. 
![](https://i.imgur.com/fiYrfYP.png)
4. Replace **YOUR_API_KEY** with your api key in *django_weather_app\config\weather\utils.py*
    ```python3
    API_KEY = 'YOUR_API_KEY'
    ```
5. ****cmd****
    ```
    > cd django_weather_app

    # Install packages
    > pipenv install

    # Start virtual envirment
    > pipenv shell
    > cd config
    
    # Start server
    > python manage.py runserver
    ````
6. Open broswer with http://127.0.0.1:8000/
![](https://i.imgur.com/knehYOj.png)