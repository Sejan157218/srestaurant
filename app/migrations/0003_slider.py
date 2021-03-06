# Generated by Django 3.1.7 on 2021-02-25 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210214_2122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=100)),
                ('title2', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=150)),
                ('date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='slider/img')),
            ],
        ),
    ]
