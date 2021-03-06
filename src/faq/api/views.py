from rest_framework import viewsets
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from ..models import Question, Tag, QuestionUpvote, Answer, AnswerUpvote
from .serializers import QuestionSerializer, TagSerializer, QuestionUpvoteSerializer, AnswerUpvoteSerializer, AnswerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Question
from ..tasks import parse_content
# Just the skeleton for now. More Work is coming


"""
    HTTP_100_CONTINUE
    HTTP_101_SWITCHING_PROTOCOLS

    HTTP_200_OK
    HTTP_201_CREATED
    HTTP_202_ACCEPTED
    HTTP_203_NON_AUTHORITATIVE_INFORMATION
    HTTP_204_NO_CONTENT
    HTTP_205_RESET_CONTENT
    HTTP_206_PARTIAL_CONTENT
    HTTP_207_MULTI_STATUS

    HTTP_300_MULTIPLE_CHOICES
    HTTP_301_MOVED_PERMANENTLY
    HTTP_302_FOUND
    HTTP_303_SEE_OTHER
    HTTP_304_NOT_MODIFIED
    HTTP_305_USE_PROXY
    HTTP_306_RESERVED
    HTTP_307_TEMPORARY_REDIRECT

    HTTP_400_BAD_REQUEST
    HTTP_401_UNAUTHORIZED
    HTTP_402_PAYMENT_REQUIRED
    HTTP_403_FORBIDDEN
    HTTP_404_NOT_FOUND
    HTTP_405_METHOD_NOT_ALLOWED
    HTTP_406_NOT_ACCEPTABLE
    HTTP_407_PROXY_AUTHENTICATION_REQUIRED
    HTTP_408_REQUEST_TIMEOUT
    HTTP_409_CONFLICT
    HTTP_410_GONE
    HTTP_411_LENGTH_REQUIRED
    HTTP_412_PRECONDITION_FAILED
    HTTP_413_REQUEST_ENTITY_TOO_LARGE
    HTTP_414_REQUEST_URI_TOO_LONG
    HTTP_415_UNSUPPORTED_MEDIA_TYPE
    HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
    HTTP_417_EXPECTATION_FAILED
    HTTP_422_UNPROCESSABLE_ENTITY
    HTTP_423_LOCKED
    HTTP_424_FAILED_DEPENDENCY
    HTTP_428_PRECONDITION_REQUIRED
    HTTP_429_TOO_MANY_REQUESTS
    HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
    HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

    HTTP_500_INTERNAL_SERVER_ERROR
    HTTP_501_NOT_IMPLEMENTED
    HTTP_502_BAD_GATEWAY
    HTTP_503_SERVICE_UNAVAILABLE
    HTTP_504_GATEWAY_TIMEOUT
    HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    HTTP_507_INSUFFICIENT_STORAGE
    HTTP_511_NETWORK_AUTHENTICATION_REQUIRED

"""


class QuestionModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ()
    filter_fields = ()


class AnswerModelViewsSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


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
    # print(data)
    author = request.user
    title = data.get('title')
    content = data.get('content')
    cat = data.getlist('category')

    try:
        q = Question.objects.create(author=author, content=content, title=title)
        for item in cat:
            q.category.add(item)
        q.save()
        response = {'success': 'Question Created Successfully'}
        stats = status.HTTP_201_CREATED
        parse_content.delay(content, q.id)
    except Exception as e:
        print(str(e))
        response = {'error': 'Question not created Successfully'}
        stats = status.HTTP_400_BAD_REQUEST
    return Response(response, status=stats)


@api_view(['POST'])
def save_reaction(request):
    data = request.data
    response_data = []
    try:
        question = Question.objects.get(id=data.get('question_id'))
        content = data.get('reaction')
    except Exception as e:
        response = {'error': 'Looks like you are answering a question that does not exist'}
        print(response)
        stat = status.HTTP_404_NOT_FOUND
    if question and content:
        try:
            a = Answer.objects.create(author=request.user, question=question, content=content)
            answer = AnswerSerializer(a)
            response_data.append(a.author)
            response_data.append(a.content)
            serialized = answer.data
            response = {'success': 'Hey Eosian, your reaction was noted, with thanks!'}
            stat = status.HTTP_201_CREATED
            parse_content.delay(content, a.id)
        except Exception as e:
            print(str(e))
            response = {'error': 'We are just finding it difficult to save your Reaction'}
            stat = status.HTTP_400_BAD_REQUEST

    return Response(response, stat)
