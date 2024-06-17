

from rest_framework import serializers
from .models import Paragraph, WordIndex

# Serializer for the Paragraph model
class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = Paragraph
        # Define the fields to be included in the serialization
        fields = ('id', 'content')

# Serializer for the WordIndex model
class WordIndexSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to be serialized
        model = WordIndex
         # Define the fields to be included in the serialization
        fields = ('id', 'word', 'paragraph_id')

