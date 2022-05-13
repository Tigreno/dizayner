from django.db import models
from django.contrib.auth.models import User

class Proizvoditeli(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Производитель")
    photo = models.ImageField(upload_to='static/photo/%Y/%m/%d/', verbose_name='фото дизайнера', blank = True)
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(default='')
    telephone = models.CharField(max_length=12, default='')

    def __str__(self) -> str:
        return self.name
