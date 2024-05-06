# Generated by Django 5.0.4 on 2024-05-04 14:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_rename_answers_answer_rename_questions_question_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testquestion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField(default=0)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('scheduled_end_time', models.DateTimeField()),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.test')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultAnalysis',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('correct_answers', models.IntegerField(default=0)),
                ('total_questions', models.IntegerField(default=0)),
                ('date_recorded', models.DateField()),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.result')),
                ('topic_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.topic')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResultAnswers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_correct', models.BooleanField(default=False)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.question')),
                ('result_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.result')),
            ],
        ),
    ]