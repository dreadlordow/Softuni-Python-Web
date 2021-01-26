from django.shortcuts import render, redirect

from .forms import RecipeForm
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def create(request):
    if request.method == 'GET':
        form = RecipeForm()
        context ={
            'form': form,
        }
        return render(request, 'create.html', context)

    else:
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

        else:
            context = {
                'form': form,
            }
            return render(request, 'create.html', context)


def edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        return render(request, 'edit.html', {'form': form})
    else:
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('index')
        form = RecipeForm(instance=recipe)
        return render(request, 'edit.html', {'form': form})


def details(request, pk):
    if request.method == 'GET':
        recipe = Recipe.objects.get(pk=pk)
        ingredients = recipe.ingredients.split(', ')
        context = {
            'recipe': recipe,
            'ingredients': ingredients,
        }
        return render(request, 'details.html', context)


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        form = RecipeForm(instance=recipe)
        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'delete.html', context)

    else:
        recipe.delete()
        return redirect('index')