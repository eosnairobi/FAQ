from rest_framework import viewsets
from ..models import Question, Tag, QuestionUpvote, Answer, AnswerUpvote
from .serializers import QuestionSerializer, TagSerializer, QuestionUpvoteSerializer, AnswerUpvoteSerializer


# Just the skeleton for now. More Work is coming

class QuestionModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all(())


class TagModelViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    queryset = TagSerializer


class QuestionUpvoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionUpvoteSerializer
    queryset = QuestionUpvote.objects.all()


class AnswerUpvoteViewSet(viewsets.ModelViewSet):
    queryset = AnswerUpvote.objects.all()
    serializer_class = AnswerUpvoteSerializer
