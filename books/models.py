from django.db import models

class Book(models.Model):
    """A model for a Book"""
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        """return the book title"""
        return self.title
