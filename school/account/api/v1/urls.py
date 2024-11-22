from django.urls import path,include
from .views import RegisterView,ProfileView
app_name='account'


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
]