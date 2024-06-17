


from django.db import models
# This model represents a paragraph of text. Each paragraph is stored as a single entry in the database.
class Paragraph(models.Model):
        # The content of the paragraph is stored as a text field.
    content = models.TextField()


# This model represents an index for words within paragraphs.
class WordIndex(models.Model):
     # The word to be indexed, stored as a character field with a maximum length of 255 characters.
    word = models.CharField(max_length=255)
     # A foreign key linking the word to the paragraph it is found in.
    # The related_name 'words' allows for reverse querying from Paragraph to WordIndex.
    # When a Paragraph is deleted, all associated WordIndex entries are also deleted (CASCADE).
    paragraph = models.ForeignKey(Paragraph, related_name='words', on_delete=models.CASCADE)
