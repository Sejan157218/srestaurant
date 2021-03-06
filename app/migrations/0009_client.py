# Generated by Django 3.1.7 on 2021-03-08 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210308_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=150)),
                ('img', models.ImageField(default='', upload_to='block')),
                ('date', models.DateField()),
            ],
        ),
    ]
