from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    # author1 = models.ForeignKey(User, on_delete=models.CASCADE) # 한 클래스 내에 두개 이상의 외래키 참조시 에러가 남
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     content = models.TextField()
#     create_date = models.DateTimeField()
#     modify_date = models.DateTimeField(null=True, blank=True)
#     question = models.ForeignKey(Question, null=True, blank=True,
#                                  on_delete=models.CASCADE)
#     answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
