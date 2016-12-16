from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib import messages

from forms import CourseForm

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
        return render(request, self.template, self.context)

    def post(self, request):
        form = self.form(data=request.POST)
        if form.is_valid():
            form.save(created_by=request.user)
            messages.add_message(request, messages.SUCCESS, _('Course created with success.'))
            response = redirect('home') 
        else:
            self.context['form'] = form
            messages.add_message(request, messages.ERROR, _('Was not possible create the course. Try again.'))
            response = render(request, self.template, self.context) 

        return response