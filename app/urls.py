from django.urls import path 
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/get-all-task/',views.get_all_task),
    path('api/add-tag/',views.add_tag),
    path('api/add-task/',views.add_task),
    path('api/todo/<int:id>/',views.TaskView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)