from django.urls import path

from randomthought import views

app_name = 'randomthought'

urlpatterns = [
    path('', views.thought, name='todays-thought'),
    path('list/', views.thought_list, name='thought-list'),
    path('create/', views.thought_create_view, name='thought-create'),
    path('update/<int:pk>/', views.thought_update_view, name='thought-update'),
    path('delete/<int:pk>/', views.thought_delete_view, name='thought-delete'),
    path('detail/<int:pk>/', views.thought_detail_view, name='thought-detail'),
]