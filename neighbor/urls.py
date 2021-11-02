from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.signup, name='signup'),
    path(r'login/', LoginView.as_view(), name='login'),
    path(r'logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path(r'^profile/', views.profile, name='profile'),
    path(r'^updateprofile/', views.update_profile, name='update_profile'),
    path(r'^newbusiness/', views.new_business, name='new_business'),
    path(r'^newpost/', views.new_post, name='new_post'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

