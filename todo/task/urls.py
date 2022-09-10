from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('create/', views.create_view, name='create'),
    path('delete/<int:id>/', views.delete_view, name='delete'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('finish/<int:id>/', views.finish_task, name='finish'),
]