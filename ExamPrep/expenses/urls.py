from django.urls import path
from expenses.views.index import index
from expenses.views.expenses import create_expense, edit_expense, delete_expense
from expenses.views.profile import delete_profile, profile_index, edit_profile, create_profile

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),


    path('profile/', profile_index, name='profile index'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]