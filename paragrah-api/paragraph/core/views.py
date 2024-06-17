


from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Paragraph, WordIndex
from .serializers import ParagraphSerializer
from django.db.models import Count

# ViewSet for handling Paragraph-related operations
class ParagraphViewSet(viewsets.ModelViewSet):
     # Define the queryset to fetch all Paragraph objects
    queryset = Paragraph.objects.all()
     # Define the serializer class to be used
    serializer_class = ParagraphSerializer

    # Override the create method to handle custom paragraph creation and word indexing
    def create(self, request, *args, **kwargs):
         # Retrieve the paragraphs text from the request data
        paragraphs_text = request.data.get('paragraphs', '')
         # Split the text into individual paragraphs based on double newline characters
        paragraphs_list = paragraphs_text.split('\n\n')

        # Loop through each paragraph text
        for paragraph_text in paragraphs_list:
            # Create a new Paragraph object with the paragraph text
            paragraph = Paragraph.objects.create(content=paragraph_text)
            words = paragraph_text.lower().split()
            for word in words:
                # Create a WordIndex entry for each word, linking it to the paragraph
                WordIndex.objects.create(word=word, paragraph=paragraph)

        # Return a success response
        return Response({'message': 'Paragraphs created successfully'}, status=status.HTTP_201_CREATED)

       # Custom action to search for paragraphs containing a specific word
    @action(detail=False, methods=['get'], url_path='search')
    def search(self, request):
         # Retrieve the search word from the query parameters and convert it to lowercase
        word = request.query_params.get('word', '').lower()

        
         # Query to get paragraphs containing the word, annotated with the count of the word occurrences
        # Order the paragraphs by the count in descending order and limit to top 10
        paragraphs = (
            Paragraph.objects.filter(words__word=word)
            .annotate(word_count=Count('words'))
            .order_by('-word_count')[:10]
        )

                # Serialize the resulting paragraphs
        serializer = self.get_serializer(paragraphs, many=True)
         # Return the serialized data in the response
        return Response(serializer.data)
