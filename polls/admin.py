from django.contrib import admin
from .models import Question
from .models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently',)
    list_filter = ['pub_date','question_text',]
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question','choice_text','votes')
    list_filter = ['question']


admin.site.register(Question, QuestionAdmin)
# Register your models here.
# admin.site.register(Question)
admin.site.register(Choice,ChoiceAdmin)
