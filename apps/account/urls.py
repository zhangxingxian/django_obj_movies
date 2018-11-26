from django.conf.urls import url

from account import views

urlpatterns = [
    url('^register/', views.register, name='register'),
    url('^login/', views.login_view, name='login'),
    url('^update/', views.update, name='update'),
    url('^mail/', views.hello_mail),
    url('^active/', views.active_account),
    url('^404/', views._404),
]