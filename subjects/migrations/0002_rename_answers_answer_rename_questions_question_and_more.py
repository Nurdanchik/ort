# Generated by Django 5.0.4 on 2024-05-03 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Answers',
            new_name='Answer',
        ),
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
        migrations.RenameModel(
            old_name='Tests',
            new_name='Test',
        ),
        migrations.RenameModel(
            old_name='TestQuestions',
            new_name='TestQuestion',
        ),
        migrations.RenameModel(
            old_name='Topics',
            new_name='Topic',
        ),
    ]
