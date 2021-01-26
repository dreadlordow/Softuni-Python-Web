from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from expenses.forms import ProfileForm
from expenses.models import Expenses, Profile


def create_profile(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()

    return redirect('index')


def profile_index(request):
    profile = Profile.objects.all()[0]
    expenses = Expenses.objects.all()
    budget = profile.budget
    all_expenses = sum(expenses.values_list('price', flat=True))
    left = budget - all_expenses
    context={
        'profile': profile,
        'left': left,
    }
    if request.method == 'GET':
        return render(request, 'profile.html', context)


def edit_profile(request):
    profile = Profile.objects.all()[0]
    if request.method == 'GET':
        form = ProfileForm(instance=profile)
        return render(request, 'profile-edit.html', {'form':form})

    else:
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile index')
        form = ProfileForm(instance=profile)
        return render(request, 'profile-edit.html', {'form': form})


def delete_profile(request):
    if request.method == 'GET':
        return render(request, 'profile-delete.html')
    else:
        Profile.objects.all()[0].delete()
        return redirect('index')
