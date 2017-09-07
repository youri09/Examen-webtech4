from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.list_all_recepten, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^add/$', views.add, name='add')
]
