from django.urls import path 
from . import views
from . import views
urlpatterns = [
    path('api/get-all-task/',views.get_all_task),
    path('api/add-tag/',views.add_tag),
    path('api/add-task/',views.add_task),
    path('api/todo/<int:id>/',views.TaskView.as_view()),
]