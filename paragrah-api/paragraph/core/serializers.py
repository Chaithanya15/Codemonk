

from rest_framework import serializers
from .models import Paragraph, WordIndex

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'content')

class WordIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordIndex
        fields = ('id', 'word', 'paragraph_id')

