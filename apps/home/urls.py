from django.conf.urls import url

from apps.home import views


urlpatterns = [
    # url('^index/', views.index, name='index'),
    url('^film/', views.TFilmView.as_view()),
    url('^cate/', views.TCateView.as_view()),
    url('^details/', views.details),
]
