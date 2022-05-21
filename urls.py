from django.urls import path

from . import views

app_name='WordleColourResult'
urlpatterns=[

	path('', views.index, name='index'),
	path('<int:result_id>', views.index, name='index'),
	path('table/', views.table, name='table'),
	
]