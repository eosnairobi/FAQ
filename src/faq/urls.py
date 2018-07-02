"""FAQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from .views import dashboard, forum, forum_list, questions, question, answer, mentions, repos, eos_911
from .api.views import (TagModelViewSet, QuestionModelViewSet, AnswerUpvoteViewSet,
                        create_faq, save_reaction, AnswerModelViewsSet)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'api/questions', QuestionModelViewSet, base_name='questions')
router.register(r'api/answers', AnswerModelViewsSet, base_name='answers')

urlpatterns = [
    path('', dashboard, name='home'),
    # path('tools/', tools, name='all_tools'),
    path('forum/', forum, name='forum'),
    path('forum-list/', forum_list, name='forum-list'),
    path('new-faq/', create_faq),
    path('eos-911/', eos_911, name='eos_911'),
    # path('dapps/', dapps, name='dapps'),
    path('save-response/', save_reaction, name='save_reaction'),
    path('github-repos/', repos, name='repos'),
    re_path(r'^questions/(?P<id>[\w-]+)/$', questions, name='cat_questions'),
    re_path(r'^question/(?P<id>[\w-]+)/$', question, name='question_detail'),
    re_path(r'^answer/(?P<id>[\w-]+)/$', answer, name='answer_detail'),
    re_path(r'^mentions/(?P<account>[\w-]+)/$', mentions, name='user_mentions'),
]


urlpatterns += router.urls
