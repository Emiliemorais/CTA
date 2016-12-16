from django import forms
from django.utils.translation import ugettext, ugettext_lazy as _
from models import Course

class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = ('name', 'duration', 'description', 'value', 'status')

    def save(self, commit=True, created_by=None):
        name = self.cleaned_data["name"]
        duration = self.cleaned_data["duration"]
        description = self.cleaned_data["description"]
        value = self.cleaned_data["value"]
        status = self.cleaned_data["status"]
        course = Course(name=name, duration=duration, description=description, value=value, 
            status=status, created_updated_by=created_by)
        if commit and created_by is not None:
            course.save()
        return course
