from django.urls import path, re_path
from .views import MainPageView, FormBuy, detail_image


urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('form_buy/', FormBuy.as_view(), name='form_buy'),
    #re_path(r'^(?P<image_id>\d+)/$', views.detail_image, name='image_detail'),
    #re_path(r'^pay/$', views.PayView.as_view(), name='pay_view'),
    #re_path(r'^pay-callback/$', views.PayCallbackView.as_view(), name='pay_callback'),
    path('<int:pk>', detail_image, name='detail_view'),
]
