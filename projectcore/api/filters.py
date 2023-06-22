from django_filters.rest_framework import FilterSet
from books.models import Book

class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {'id':['exact'],
                  'pub_year':['exact'],
                  'title':['']
                  }