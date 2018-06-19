from django.db import models
import uuid
from django.conf import settings
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Definition of the Questions + Answers


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='asked_by', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='created_time', blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=140)
    respondent = models.ManyToManyField(settings.AUTH_USER_MODEL)
    created_time = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')

    def save(self, *args, **kwargs):
        # Override save (to define a slug)
        if not self.slug:
            self.slug = slugify(self.title)
            super(Question, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.content

    def get_total_upvotes(self):
        return self.question_upvote.all().count()


class Respondent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30, blank=True)
    account_name = models.CharField(max_length=12)


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    count = models.PositiveIntegerField(default=0)
    question = models.ManyToManyField(Question)

    def __str__(self):
        return self.name


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='answered_by', on_delete=models.CASCADE)
    upvoted = models.BooleanField(default=False)

    # def __str__(self):
    # return self.


class QuestionUpvote(models.Model):
    question = models.OneToOneField(Question, related_name='question_upvote', on_delete=models.CASCADE)
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='voted_by', on_delete=models.CASCADE)


class AnswerUpvote(models.Model):
    answer = models.OneToOneField(Answer, related_name='answer_upvote', on_delete=models.CASCADE)
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='upvoted_by', on_delete=models.CASCADE)
