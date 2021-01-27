from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from expenses.forms import ProfileForm, ExpensesForm
from expenses.models import Profile, Expenses


def create_expense(request):
    if request.method == 'GET':
        form = ExpensesForm()
        context = {
            'form': form
        }
        return render(request, 'expense-create.html', context)

    else:
        form = ExpensesForm(request.POST)
        expenses = Expenses.objects.all()
        profile = Profile.objects.all()[0]
        budget = profile.budget
        all_expenses = sum(expenses.values_list('price', flat=True)) + int(request.POST['price'])

        if form.is_valid():
            expense = form.save(commit=False)
            expense.profile = profile
            expense.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expenses.objects.get(pk=pk)
    if request.method == 'GET':
        form = ExpensesForm(instance=expense)
        context={
            'form': form,
        }
        return render(request, 'expense-edit.html',context)
    else:
        form = ExpensesForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form,
        }
        return render(request, 'expense-edit.html', context)

    pass


def delete_expense(request, pk):
    expense = Expenses.objects.get(pk=pk)
    form = ExpensesForm(instance=expense)
    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': form,
        }
        return render(request, 'expense-delete.html', context)

    else:
        expense.delete()
        return redirect('index')