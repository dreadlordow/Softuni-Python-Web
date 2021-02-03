from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.decorators import user_required
from .forms import PetForm, CommentForm
from .models import Pet, Comment
from .models import Like


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }

    return render(request, 'pet_list.html', context)


@login_required
def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        pet.likes_count = pet.like_set.count()
        context = {
            'pet': pet,
            'form': CommentForm(),
            'can_delete': request.user == pet.user.user,
            'can_edit': request.user == pet.user.user,
            'can_like': request.user != pet.user.user,
            'has_liked': pet.like_set.filter(user_id=request.user.userprofile.id).exists(),
            'can_comment': request.user != pet.user.user,

        }
        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.user = request.user.userprofile
            comment.save()
            return redirect('pet details', pk)
        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pet_detail.html', context)


@login_required
def like_pet(request, pk):
    like = Like.objects.filet(user_id=request.user.userprofile.id, pet_id=pk).first()
    if like:
        like.delete()
    else:
        pet = Pet.objects.get(pk=pk)
        like = Like(test=str(pk), user=request.user.userprofile)
        like.pet = pet
        like.save()
        return redirect('list pets')


@login_required
def create(request):
    if request.method == 'GET':
        form = PetForm()
        context = {
            'form': form
        }
        return render(request, 'pet_create.html', context)

    else:
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list pets')
        context = {
            'form': form
        }
        return render(request, 'pet_create.html', context)


@user_required(Pet)
def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        if request.user != pet.user.user:
            return HttpResponseNotFound('<h1>Access denied<h1>')
        form = PetForm(instance=pet)

        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pet_edit.html', context)
    else:
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()

        return redirect('pet details', pet.pk)


@login_required
def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if pet.user.user != request.user:
        return HttpResponseNotFound('<h1>Access denied<h1>')
    if request.method == 'GET':
        context ={
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')