from django.urls import path

from randomthought import views

app_name = 'randomthought'

urlpatterns = [
    path('', views.thought, name='todays_thought'),
]