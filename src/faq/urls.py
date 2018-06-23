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
from django.urls import path
from .views import dashboard, forum, forum_list
from .api.views import TagModelViewSet, QuestionModelViewSet, AnswerUpvoteViewSet, create_faq, save_reaction, AnswerModelViewsSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'question', QuestionModelViewSet, base_name='question')
router.register(r'answer', AnswerModelViewsSet, base_name='answers')

urlpatterns = [
    path('home/', dashboard),
    path('forum/', forum, name='forum'),
    path('forum-list/', forum_list, name='forum-list'),
    path('new-faq/', create_faq),
    path('save-response/', save_reaction, name='save_reaction'),
]


urlpatterns += router.urls
