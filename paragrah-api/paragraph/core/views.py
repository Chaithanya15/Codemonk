


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Paragraph, WordIndex
from .serializers import ParagraphSerializer
from django.db.models import Count

class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

    def create(self, request, *args, **kwargs):
        paragraphs_text = request.data.get('paragraphs', '')
        paragraphs_list = paragraphs_text.split('\n\n')

        for paragraph_text in paragraphs_list:
            paragraph = Paragraph.objects.create(content=paragraph_text)
            words = paragraph_text.lower().split()
            for word in words:
                WordIndex.objects.create(word=word, paragraph=paragraph)

        return Response({'message': 'Paragraphs created successfully'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
        word = request.query_params.get('word', '').lower()

        # Query to get paragraphs containing the word, ordered by frequency
        paragraphs = (
            Paragraph.objects.filter(words__word=word)
            .annotate(word_count=Count('words'))
            .order_by('-word_count')[:10]
        )

        serializer = self.get_serializer(paragraphs, many=True)
        return Response(serializer.data)
