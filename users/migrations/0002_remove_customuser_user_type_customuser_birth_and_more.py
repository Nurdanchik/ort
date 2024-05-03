# Generated by Django 5.0.4 on 2024-04-26 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birth',
            field=models.DateField(default='2006-01-01'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='User', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='school',
            field=models.CharField(default='No school', max_length=128),
        ),
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=7),
        ),
        migrations.AddField(
            model_name='customuser',
            name='subscription_status',
            field=models.BooleanField(default=False),
        ),
    ]