from django.conf.urls import url

from home import views

urlpatterns = [
    url('^index', views.index, name='index')
]
