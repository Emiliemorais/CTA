from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^create_course/', views.CourseView.as_view(), name='create_course'),
    url(r'^courses/', views.CourseView().get_courses, name='courses'),
    url(r'^edit_course/(?P<course_id>\d+)$', views.CourseView().edit_course, name='edit_course'),
    url(r'^update_course/(?P<course_id>\d+)$', views.CourseView().update_course, name='update_course'),
]