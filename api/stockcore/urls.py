from django.conf.urls import url

from stockcore import views

urlpatterns = [
    url(r'^$', views.IndexList.as_view()),
    url(r'^stocks/get/$', views.StockList.as_view()),
    url(r'^stocks/save/$', views.StockPost.as_view()),
]
