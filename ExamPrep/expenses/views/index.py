from django.shortcuts import render

from expenses.forms import ProfileForm
from expenses.models import Expenses, Profile


def index(request):
    profile = Profile.objects.exists()
    form = ProfileForm()
    if not profile:
        return render(request, 'home-no-profile.html', {'form': form, 'profile': profile})

    elif profile:
        expenses = Expenses.objects.all()
        current_profile = Profile.objects.all()[0]
        budget = current_profile.budget
        total = budget - sum(expenses.values_list('price', flat=True))
        context = {
            'form': form,
            'profile': current_profile,
            'total': total,
            'expenses': expenses,
        }
        return render(request, 'home-with-profile.html', context)
