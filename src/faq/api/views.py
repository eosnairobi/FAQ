from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from ..models import Question, Tag, QuestionUpvote, Answer, AnswerUpvote
from .serializers import QuestionSerializer, TagSerializer, QuestionUpvoteSerializer, AnswerUpvoteSerializer


# Just the skeleton for now. More Work is coming

class QuestionModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ()
    filter_fields = ()


class TagModelViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = TagSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ()
    filter_fields = ()


class QuestionUpvoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionUpvoteSerializer
    queryset = QuestionUpvote.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('')
    filter_fields = ('')


class AnswerUpvoteViewSet(viewsets.ModelViewSet):
    queryset = AnswerUpvote.objects.all()
    serializer_class = AnswerUpvoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('')
    filter_fields = ('')
