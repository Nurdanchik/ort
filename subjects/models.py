from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='media/', default='none.png')
    description = models.TextField()

    def __str__(self):
        return self.subject_name

class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    EASY = 'EASY'
    MIDDLE = 'MIDDLE'
    HARD = 'HARD'
    ADVANCED = 'ADVANCED'
    SCALE = (
        (EASY,'EASY'),
        (MIDDLE, 'MIDDLE'),
        (HARD, 'HARD'),
        (ADVANCED, 'Advanced')
    )

    topic_name = models.CharField(max_length=128)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/', default='none.png')
    description = models.TextField()
    question_type = models.CharField(choices=SCALE, default=EASY, max_length=20, verbose_name=_("Difficulty"))

    def __str__(self):
        return self.topic_name

class Test(models.Model):
    id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=255, default=_("New test"))
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_duration_minutes = models.TimeField(default='00:00:00')

    def __str__(self):
        return self.test_name

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.TextField()
    image = models.ImageField(upload_to='media/', default='none.png')
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class TestQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(Question, related_name="answer", on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to='media/', default='none.png')

class Result(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    scheduled_end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.id}'

class ResultAnalysis(models.Model):
    id = models.AutoField(primary_key=True)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    date_recorded = models.DateField()

class ResultAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    result_id = models.ForeignKey(Result, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)