# this is like a datebase layout
from django.db import models


# Create your models here.
class Question(models.Model):
    objects = None
    question_text = models.CharField(max_length=200)  # question_text
    pub_date = models.DateTimeField('date published')  # publish_date

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)  # choice_text
    votes = models.IntegerField(default=0)  # numberOfVotes
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # link

    def __str__(self):
        return self.choice_text
