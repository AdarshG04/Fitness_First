# Generated by Django 5.1.1 on 2024-11-10 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0003_alter_fitnessmetric_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fitnessmetric',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], help_text='Select your gender', max_length=1),
        ),
    ]
