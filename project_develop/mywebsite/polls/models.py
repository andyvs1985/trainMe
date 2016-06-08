import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Date is published')
    my_mail = models.EmailField(max_length=254, blank=True)
    Name = models.CharField(max_length=200)
    Age = models.IntegerField()
    Height = models.FloatField()
    Weight = models.FloatField()

    def __str__(self): # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self): # __unicode__ on Python 2
        return self.Name

    def __int__(self): # __unicode__ on Python 2
        return self.Age    

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self): # __unicode__ on Python 2
        return self.choice_text

class Answer(models.Model):
    answer = models.ForeignKey(Choice)
    answer_text = models.CharField(max_length=200)

    def __unicode__(self): # __unicode__ on Python 2
        return self.answer_text