# Установка
1) Обновить pip
`python -m pip install --upgrade pip`
2) Установить PostgreSQL и установить
`pip install psycopg2`
3) В файле `settings.py` в разделе `DATABASES` изменить данные под свою таблицу
```
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'django_db',
'USER' : 'user_name',
'PASSWORD' : 'password',
'HOST' : '127.0.0.1',
'PORT' : '5432',
```
4) Установить виртуальное окружение
`pip install virtualenv`
Создать новый virtualenv
`virtualenv yourenvname -p python<версия python>`
Активировать виртуальную среду
`source yourenvname/bin/activate`
5) Установить Django и Django rest framework
`pip install django djangorestframework`
6) Установить Djoser: REST-реализация системы аутентификации Django.
`pip install djoser`
7) Установить серверную часть аутентификации веб-токена JSON для REST Framework Django
`pip install djangorestframework_simplejwt`

8) Для запуска написать
`python manage.py runserver`
