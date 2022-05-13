# Generated by Django 4.0.4 on 2022-04-23 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dizayner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(verbose_name='Описание')),
                ('dizayner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dizayner.dizayner', verbose_name='Дизайнер')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='static/photo/%Y/%m/%d/', verbose_name='фото дизайнера')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dizayner.portfolio', verbose_name='Портфолио')),
            ],
        ),
    ]
