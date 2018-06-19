from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from ..models import Question, Tag, QuestionUpvote, Answer, AnswerUpvote
from .serializers import QuestionSerializer, TagSerializer, QuestionUpvoteSerializer, AnswerUpvoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Question

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


@api_view(['POST', ])
def create_faq(request):
    data = request.data
    print(data)
    author = request.user
    title = data.get('title')
    content = data.get('content')
    try:
        q = Question.objects.create(author=author, content=content, title=title)
        response = {'success': 'Question Created Successfully'}
    except:
        response = {'error': 'Question not created Successfully'}
    return Response(response)


# class Question(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='asked_by', on_delete=models.CASCADE)
#     slug = models.SlugField(max_length=250, unique_for_date='created_time', blank=True)
#     title = models.CharField(max_length=200)
#     content = models.TextField(max_length=140)
#     respondent = models.ManyToManyField(settings.AUTH_USER_MODEL)
#     created_time = models.DateTimeField(auto_now_add=True)
#     edited = models.DateTimeField(auto_now=True)
#     liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='liked')
