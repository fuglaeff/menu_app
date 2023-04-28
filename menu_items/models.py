from django.core.exceptions import ValidationError
from django.db import models


class Menu(models.Model):
    slug = models.SlugField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class MenuItem(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='folders'
    )

    class Meta:
        ordering = ('name', )

    def clean(self):
        if self.parent and self.parent.menu != self.menu:
            raise ValidationError('Parent menu must eq menu')

    def __str__(self):
        return self.name
