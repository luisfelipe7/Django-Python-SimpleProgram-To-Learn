from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
# Version 1
# admin.site.register(Question)
# admin.site.register(Choice)

# Version 2
# class QuestionAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question_text']

# Version 3, Divide the form in different part with several fields

# StackedInLine is a way to display the data, it is more usefull to use admin.TabularInline


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3  # Provide enough fields for 3 choices and each time you
    # come back to the “Change” page for an already-created object, you get another three extra slots.

# Without choices
# class QuestionAdmin(admin.ModelAdmin):
#    fieldsets = [
#        # Title, Fields
#        (None, {'fields': ['question_text']}),
#        ('Date Information', {'fields': ['pub_date']})
#    ]

# With choices


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        # Title, Fields
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    # This is for change the page where the admin site display the list of questions, this is only for the list
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
