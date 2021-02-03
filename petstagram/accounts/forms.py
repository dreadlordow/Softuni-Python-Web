from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import UserProfile


class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all()

    def add_form_control_class_to_all(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', )
