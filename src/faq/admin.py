from django.contrib import admin

from .models import Question, Answer, QuestionUpvote, AnswerUpvote, Category

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(AnswerUpvote)
admin.site.register(QuestionUpvote)
admin.site.register(Category)
