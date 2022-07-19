from django.urls import path
from .views import *
# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'home'
urlpatterns = [
    path('', home, name='home'),
    path('hotel-detail/<uid>/' , hotel_detail , name="hotel_detail"),
    path('login/', login_page, name='loginpage'),
    path('register/', register_page, name='register-page')
 ]