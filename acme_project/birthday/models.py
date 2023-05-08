from django.db import models
from django.urls import reverse

from .validators import real_age

class Birthday(models.Model):
    first_name = models.CharField(verbose_name='Имя', max_length=20)
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=20,
        blank=True,
        help_text='Необязательное поле'
    )
    birthday = models.DateField(verbose_name='Дата рождения', validators=(real_age,))
    image = models.ImageField(verbose_name='Фото', blank=True, upload_to='birthday_images')
    
    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('first_name', 'last_name', 'birthday'),
                name='Unique person constrains',
            ),
        )
    
    def get_absolute_url(self):
        return reverse("birthday:detail", kwargs={"pk": self.pk})
    
    