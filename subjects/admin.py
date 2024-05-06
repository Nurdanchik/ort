from django.contrib import admin
from .models import Topic, Subject, Test, Question, TestQuestion, Answer, Result, ResultAnswer, ResultAnalysis

class AnswerInlineModel(admin.TabularInline):
    model = Answer
    fields = [
        'answer_text',
        'is_correct'
    ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text']
    inlines = [
        AnswerInlineModel,
    ]

admin.site.register(Topic)
admin.site.register(Subject)
admin.site.register(Test)
admin.site.register(TestQuestion)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(ResultAnalysis)
admin.site.register(ResultAnswer)