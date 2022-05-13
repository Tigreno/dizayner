from pickle import TRUE
from django.db import models
from django.urls import reverse
from .dizayner import Dizayner

class Portfolio(models.Model):
    dizayner = models.ForeignKey(Dizayner, on_delete=models.CASCADE, verbose_name='Дизайнер')
    name = models.CharField(max_length=128)
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return str(self.dizayner) + ' ' + self.name

    def get_absolute_url(self):
        return reverse('dizayner:portfolio_detail', kwargs={'dizayner_id' : self.dizayner.id , 'portfolio_id' : self.pk})

class Portfolio_photo(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, verbose_name='Портфолио')
    description = models.TextField(verbose_name='Описание', default='', blank=TRUE)
    image = models.ImageField(upload_to='static/photo/%Y/%m/%d/', verbose_name='фото дизайнера')