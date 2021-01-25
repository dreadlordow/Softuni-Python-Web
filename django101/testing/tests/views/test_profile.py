from django.test import TestCase, Client
from django.urls import reverse

from testing.models import Profile


class PersonViewsTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getIndex_shouldRendercorrectTemplateWithNoProfiles(self):
        response = self.test_client.get(reverse('profiles'))
        self.assertTemplateUsed(response, 'testing/index.html')
        profiles = response.context['profiles']
        self.assertEqual(0, len(profiles))

        form = response.context['form']
        self.assertIsNotNone(form)

    def test_getIndex_shouldRendercorrectTemplateWithProfiles(self):
        profiles = (
            Profile(name='d',age=1, egn='1234567890'),
            Profile(name='m',age=1, egn='023456789'),
        )
        [profile.save() for profile in profiles]

        response = self.test_client.get(reverse('profiles'))
        self.assertTemplateUsed(response, 'testing/index.html')
        profiles = response.context['profiles']
        self.assertEqual(2, len(profiles))

        form = response.context['form']
        self.assertIsNotNone(form)

    def test_postIndex_whenValidData_shouldRedirectToIndex(self):
        name = 'Georgi'
        age = 21
        egn = '1234567890'
        data={
            'name': name,
            'age': age,
            'egn': egn,
        }
        response = self.test_client.post(reverse('profiles'), data=data)
        self.assertRedirects(response, reverse('profiles'))

    def test_postIndex_whenValidDataContainsLetter_shouldRenderIndexAndContainsErrors(self):
        name = 'Georgi'
        age = 21
        egn = '123456789a'
        data={
            'name': name,
            'age': age,
            'egn': egn,
        }
        response = self.test_client.post(reverse('profiles'), data=data)

        self.assertTemplateUsed(response, 'testing/index.html')
        profiles = response.context['profiles']
        self.assertEqual(0, len(profiles))

        form = response.context['form']
        self.assertIsNotNone(form.errors['egn'])