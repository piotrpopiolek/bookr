# Generated by Django 4.1.3 on 2022-11-19 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nazwa wydawnictwa', max_length=50)),
                ('website', models.URLField(help_text='Witryna wydawnictwa')),
                ('email', models.EmailField(help_text='Adres e-mail', max_length=254)),
            ],
        ),
    ]
