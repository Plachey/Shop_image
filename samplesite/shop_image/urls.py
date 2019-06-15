from django.urls import path
from .views import MainPageView, FormBuy, detail_image


urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('form_buy/', FormBuy.as_view(), name='form_buy'),
    path('<int:pk>', detail_image, name='detail_view'),
]

"REST, PEP8, API, FLASK, SANIC, МИКРОСЕРВИС. АРХИТЕКТ., - read"

'''
Auth service
ETL
Project service
Calcul. service

RestFull Flask
Redis - для авториз. сервиса
Celery / RebbitMQ - для калькул. сервис
SQLAlchemy ORM
Postgres

'''

среда пятница на 10