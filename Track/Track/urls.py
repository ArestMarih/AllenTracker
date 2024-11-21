
from django.contrib import admin
from django.urls import path
from trak.views import TaskAPI
from trak import views

urlpatterns = [
    path('admin/', admin.site.urls),
   #  path('', main, name='main'),
   #  path('deleters/<int:id>/', views.deleters),
    path('api/v1/task', TaskAPI.as_view()),
    path('api/v1/task/<int:pk>',view=TaskAPI.as_view())
    
]
