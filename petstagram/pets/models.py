from django.db import models


class Pet(models.Model):
    DOG = 'dog'
    CAT = 'cat'
    PARROT = 'parrot'
    UNKNOWN = 'unknown'
    PET_TYPES = (
        (DOG, 'Dog'),
        (CAT, 'cat'),
        (PARROT, 'parrot'),
        (UNKNOWN, 'unknown')
    )
    type = models.CharField(max_length=7, choices=PET_TYPES, default=UNKNOWN)
    name = models.CharField(max_length=6, blank=False)
    age = models.IntegerField(blank=False)
    description = models.TextField(blank=False)
    image_url = models.ImageField(blank=False, upload_to='pets')

    def __str__(self):
        return f'{self.id}; {self.name}; {self.age}'


class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    test = models.CharField(max_length=10)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=False)