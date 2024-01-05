# Generated by Django 4.2 on 2024-01-05 04:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', models.DateField(default=django.utils.timezone.now)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.region')),
            ],
        ),
    ]
