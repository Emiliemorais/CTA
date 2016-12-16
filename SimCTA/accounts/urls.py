from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
	url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
]