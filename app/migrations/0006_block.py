# Generated by Django 3.1.7 on 2021-03-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blocktitle', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('blockdesc', models.CharField(max_length=150)),
                ('desc', models.CharField(max_length=150)),
                ('img', models.ImageField(default='', upload_to='block')),
                ('date', models.DateField()),
            ],
        ),
    ]
