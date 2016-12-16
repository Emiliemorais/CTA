from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^create_course/', views.CourseView.as_view(), name='create_course'),
]