# Generated by Django 4.0.1 on 2022-06-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('book_price', models.IntegerField()),
                ('book_category', models.CharField(max_length=100)),
            ],
        ),
    ]