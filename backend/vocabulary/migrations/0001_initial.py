# Generated by Django 3.2.13 on 2023-03-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('word', models.CharField(max_length=55)),
                ('mean', models.CharField(max_length=103)),
            ],
        ),
    ]
