# Generated by Django 4.2.9 on 2024-08-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]
