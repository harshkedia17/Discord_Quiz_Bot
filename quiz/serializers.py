from pyexpat import model
from re import M
from attr import fields
from rest_framework import serializers
from .models import Answer, Question 

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'id',
            'answer',
            'is_correct'
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many = True, read_only = True)
    class Meta:
        model = Question
        fields = [
            'title','answer'
        ]    