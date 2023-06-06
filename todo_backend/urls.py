

from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include("app.urls")),
    # path('api/todo/<int:id>/',views.TaskView.as_view()),

]
