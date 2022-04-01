from django.urls import path

from randomthought import views

app_name = 'randomthought'

urlpatterns = [
    path('', views.todays_thought, name='todays_thought'),
]