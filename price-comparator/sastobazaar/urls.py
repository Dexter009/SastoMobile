
from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^search_results/$', views.search_result, name="search_results"),
]

