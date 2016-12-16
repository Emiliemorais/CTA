from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import messages

from forms import CourseForm
from models import Course

def home(request):
    # Put the classes here
    return render(request, "home.html", {})


class CourseView(View):

    form = CourseForm
    template = "new_course.html"

    context = {
        'form': form
    }
    def get(self, request):
        self.context['submit_text'] = _('Create')
        self.context['cancel_url'] = 'home'
        return render(request, self.template, self.context)

    def post(self, request):
        messages = {
            'success': _('Course created with success.'),  
            'failure': _('Was not possible create the course. Try again.')
        }
        response = self.save_course(request, form, messages)

        return response

    def get_courses(self, request):
        active_courses = Course.objects.filter(status=True)
        inactive_courses = Course.objects.filter(status=False)

        context = {
            'active_courses': active_courses,
            'inactive_courses': inactive_courses
        }

        return render(request, 'show_courses.html', context)

    def edit_course(self, request, course_id=None):
        course = Course.objects.get(pk=course_id)
        form = self.form(instance=course)
        self.context['form'] = form
        self.context['course'] = course
        self.context['submit_text'] = _('Edit')
        self.context['cancel_url'] = 'courses'
        return render(request, "edit_course.html", self.context)

    def update_course(self, request, course_id=None):
        messages = {
            'success': _('Course updated with success.'),  
            'failure': _('Was not possible update the course. Try again.')
        }
        response = self.save_course(request, form, messages)

        return response

    def save_course(self, request, message):
        form = self.form(data=request.POST)
        if form.is_valid():
            form.save(created_by=request.user)
            messages.add_message(request, messages.SUCCESS, message['success'])
            response = redirect('home') 
        else:
            self.context['form'] = form
            messages.add_message(request, messages.ERROR, message['failure'])
            response = render(request, self.template, self.context) 

        return response
