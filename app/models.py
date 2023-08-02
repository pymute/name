from django.db import models

from datetime import datetime

class QuestionModel(models.Model):
    question_text = models.CharField(max_length=150,default='')
    pub_date = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table= 'question'
