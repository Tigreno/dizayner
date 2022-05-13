import datetime
from django.db import models
from django.contrib.auth.models import User


class Dizayner(models.Model):
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Дизайнер')
    photo = models.ImageField(upload_to='static/photo/%Y/%m/%d/', verbose_name='фото дизайнера')
    birthday = models.DateField(verbose_name='Дата рождения')
    email = models.EmailField(default='')
    telephone = models.CharField(max_length=12, default='')
    
    def __str__(self) -> str:
        return self.last_name + " " + self.name

    def age(self):
        delta = datetime.datetime.now() - self.birthday
        return delta.years
    
    


