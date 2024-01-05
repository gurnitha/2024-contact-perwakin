# Generated by Django 4.2 on 2024-01-05 03:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]