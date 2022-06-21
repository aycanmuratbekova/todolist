from django.urls import path
from .views import index, addTodo, complete_todo, delete_completed, delete_all

urlpatterns = [
    path('', index, name='index'),
    path('add', addTodo, name='add'),
    path('complete/<todo_id>', complete_todo, name='complete'),
    path('delete_complete', delete_completed, name='deletecomplete'),
    path('delete_all', delete_all, name='deleteall'),
]

