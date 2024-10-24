# Generated by Django 5.1.1 on 2024-10-22 18:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metrics', '0002_delete_fitnessmetric'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FitnessMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('waist_circumference', models.FloatField()),
                ('hip_circumference', models.FloatField()),
                ('bmi', models.FloatField(blank=True, help_text='Body Mass Index', null=True)),
                ('whr', models.FloatField(blank=True, help_text='Waist-to-Hip Ratio', null=True)),
                ('whtr', models.FloatField(blank=True, help_text='Waist-to-Height Ratio', null=True)),
                ('date_calculated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
