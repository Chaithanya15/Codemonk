


from django.db import models

class Paragraph(models.Model):
    content = models.TextField()

class WordIndex(models.Model):
    word = models.CharField(max_length=255)
    paragraph = models.ForeignKey(Paragraph, related_name='words', on_delete=models.CASCADE)
