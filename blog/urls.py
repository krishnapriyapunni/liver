from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('',views.index,name='index'),
	path('signup/',views.signup,name='signup'),
	path('login/',views.log_in,name='login'),
	path('signup1/',views.signup1,name='signup1'),
	path('login1/',views.log_in1,name='login1'),
	path('about/',views.about,name='about'),
	path('index/',views.index,name='index'),
	# path('prediction',views.prediction,name='prediction'),
	path('contact/',views.contact,name='contact'),
	# path('index1/',views.index1,name='index1'),
	path('clinicalmanager/',views.clinicalmanager,name='clinicalmanager'),
	path('details/',views.details,name='details'),
	path('regional/',views.regional,name='regional'),
	path('prediction/',views.prediction,name='prediction'),
	path('source/',views.source,name='source'),
	path('result/',views.result,name='result'),
	# path('gallery/',views.gallery,name='gallery'),
	path('uploads/simple/',views.simple_upload, name='simple_upload'),
	# path('uploads/simple/',views.simple_upload, name='simple_upload'),

	# path('result/',views.result, name='result'),
	# path('prediction1/',views.prediction1, name='prediction1'),
]
#  url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
