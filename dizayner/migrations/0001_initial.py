# Generated by Django 4.0.4 on 2022-04-23 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dizayner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('photo', models.ImageField(upload_to='static/photo/%Y/%m/%d/', verbose_name='фото дизайнера')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Дизайнер')),
            ],
        ),
    ]