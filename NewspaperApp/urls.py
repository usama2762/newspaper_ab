from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('a',views.index,name='index'),
	path('articleDetail',views.detail,name='detail'),
	path('<str:random_string>',views.dummy_view1),
]
