from django.test import TestCase

from testing.forms.profile import ProfileForm


class ProfileFormTests(TestCase):
    def test_saveProfileForm_whenValidEgn(self):
        name='Georgi'
        age= 21
        egn = '1234567890'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertTrue(form.is_valid())

    def test_saveProfileForm_when_contains_letter_should_be_invalid(self):
        name='Georgi'
        age= 21
        egn = '12345678a0'
        form = ProfileForm(data={
            'name':name,
            'age':age,
            'egn':egn,
        })

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_when_egn_contains_less_digits_should_be_invalid(self):
        name='Georgi'
        age= 21
        egn = '123456'
        form = ProfileForm(data={
            'name':name,
            'age':age,
            'egn':egn,
        })

        self.assertFalse(form.is_valid())


    def test_saveProfileForm_when_egn_contains_11_digits_should_be_invalid(self):
        name='Georgi'
        age= 21
        egn = '12345678901'
        form = ProfileForm(data={
            'name':name,
            'age':age,
            'egn':egn,
        })

        self.assertFalse(form.is_valid())
