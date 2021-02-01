from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PetForm, CommentForm
from .models import Pet, Comment
from .models import Like


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }

    return render(request, 'pet_list.html', context)


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        pet.likes_count = pet.like_set.count()
        context = {
            'pet': pet,
            'form': CommentForm()
        }
        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details', pk)
        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('list pets')


def create(request):
    if request.method == 'GET':
        form = PetForm()
        context = {
            'form': form
        }
        return render(request, 'pet_create.html', context)

    else:
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list pets')
        context = {
            'form': form
        }
        return render(request, 'pet_create.html', context)


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pet_edit.html', context)
    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()

        return redirect('pet details', pet.pk)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context ={
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')