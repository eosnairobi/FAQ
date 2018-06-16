from rest_framework import viewsets
from ..models import Question, Tag
from .serializers import QuestionSerializer, TagSerializer


# Just the skeleton for now. More Work is coming

class QuestionModelViewSet(viewsets.ModelViewSet):
    pass


class TagModelViewSet(viewsets.ModelViewSet):
    pass
