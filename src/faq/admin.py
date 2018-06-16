from django.contrib import admin

from .models import Question, Answer, QuestionUpvote, AnswerUpvote

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerUpvote)
admin.site.register(QuestionUpvote)
