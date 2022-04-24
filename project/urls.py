from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.register,name="regi"),
    path('login/',views.auth_login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('changepass/',views.update_password,name="changepass"),
    path('userprofile/',views.user_profile,name="userprofile"),
]
