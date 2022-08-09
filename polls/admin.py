from django.contrib import admin
from . models import Question, Choice
from django.contrib.auth.models import User


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text','pub_date','was_published_recently')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)




