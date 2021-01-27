from django import forms

from expenses.models import Profile, Expenses


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = '__all__'
        exclude = ('profile',)
