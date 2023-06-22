from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import Bookserializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .pagination import BookListPagination
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# @api_view(['GET'])
# def listitem(request):
#     books = Book.objects.all()
#     serializer = Bookserializer(books, many=True)
#     return Response(serializer.data)

class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403, 'errors':serializer.errors, 'message':'something wrong'})
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj), 'message':'your data is saved'})

@api_view(['POST'])
def additem(request):
    serializer = Bookserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateitem(request,pk):
    books = Book.objects.get(id=pk)
    serializer = Bookserializer(instance=books,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteitem(request,pk):
    books = Book.objects.get(id=pk)
    books.delete()
    return Response('Item deleted successfully')


class Booklist(ListAPIView):
    queryset          = Book.objects.all()
    serializer_class  = Bookserializer
    filter_backends   = (DjangoFilterBackend,OrderingFilter)
    filterset_fields  = ['id','pub_year','title']
    ordering_fields     = ['id','pub_year','title']
    pagination_class  = BookListPagination

    