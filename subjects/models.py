from django.db import models
from django.utils.translation import gettext_lazy as _


# SCALE = (
#     (0, _('Fundamental')),
#     (1, _('Beginner')),
#     (2, _('Intermediate')),
#     (3, _('Advanced')),
#     (4, _('Expert'))
# )
# TYPE = (
#     (0, _('Multiple Choice')),
# )
# quiz = models.ForeignKey(Test, related_name='question', on_delete=models.DO_NOTHING)
# techniques = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of Question"))
# title = models.CharField(max_length=255, verbose_name=_("Title"))
# difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Difficulty"))
# date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
# is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

class Subjects(models.Model):
    id = models.AutoField()
    subject_name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='images/', default='none.png')
    description = models.TextField()

    def __str__(self):
        return self.subject_name

class Topics(models.Model):
    SCALE = (
        (0, _('EASY')),
        (1, _('MIDDLE')),
        (2, _('HARD')),
        (3, _('Advanced'))
    )

    id = models.AutoField()
    topic_name = models.CharField(max_length=128)
    subject_id = models.ForeignKey(Subjects)
    image = models.ImageField(upload_to='images/', default='none.png')
    description = models.TextField()
    question_type = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Difficulty"))

class Tests(models.Model):
    id = models.AutoField()
    test_name = models.CharField(max_length=255, default=_("New test"))
    subject_id = models.ForeignKey(Subjects)
    test_duration_minutes = models.TimeField()

    def __str__(self):
        return self.test_name

class Questions(models.Model):
    id = models.AutoField()
    question_text = models.TextField()
    image = models.ImageField(upload_to='images/', default='none.png')
    topic_id = models.ForeignKey(Topics)

    def __str__(self):
        return self.question_text

class TestQuestions(models.Model):
    id = models.AutoField()
    test_id = models.ForeignKey(Tests)
    question_id = models.ForeignKey(Questions)


class Answers(models.Model):
    id = models.AutoField()
    question_id = models.ForeignKey(Questions, related_name="answer", on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', default='none.png')
