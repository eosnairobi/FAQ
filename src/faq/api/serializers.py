from rest_framework import serializers
from ..models import Question, Tag, Answer, AnswerUpvote, QuestionUpvote


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


class AnswerUpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerUpvote
        fields = '__all__'


class QuestionUpvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionUpvote
        fields = '__all__'
