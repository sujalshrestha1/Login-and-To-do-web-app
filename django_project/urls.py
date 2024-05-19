from django.urls import path
from myapp import views  # Replace app_name with the actual name of your app
from django.contrib import admin

urlpatterns = [
    path('', views.index_view, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_view, name='delete_todo'),
]
