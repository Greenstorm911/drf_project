# Generated by Django 4.2.9 on 2024-06-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
