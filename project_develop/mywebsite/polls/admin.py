from django.contrib import admin

# Register your models here.

from .models import Question, Choice, Answer

class QuestionAdmin(admin.ModelAdmin):
    #fieldsets = [
    fields = ['question_text', 'pub_date','my_mail', 'Name', 'Age', 'Height', 'Weight']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Answer)

