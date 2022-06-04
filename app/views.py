from django.shortcuts import render,redirect
from .forms import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BooksSerializer

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addshow')
    else:
        form = UserForm()
    return render(request,'login.html',{'form':form})

def addshow(request):
    if request.method == "POST": 
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addshow')
    else: 
        form = BookForm()
    show = Books.objects.all()
    return render(request,'addshow.html',{'form':form,'ash':show})

def delete(request,id):
   if request.method == "POST":
       books = Books.objects.get(id=id)
       books.delete()
       return redirect('addshow')
   
def update(request,id):
    if request.method == "POST":
        books = Books.objects.get(id=id)
        form = BookForm(request.POST,instance=books)
        if form.is_valid():
            form.save()
            return redirect('addshow')
    else:
        books = Books.objects.get(id=id)
        form = BookForm(instance=books)
    return render(request,'update.html',{'form':form})

def student(request):
    stu = Books.objects.all()
    return render(request,'student.html',{'ash':stu})
    
@api_view(['GET'])
def Book_get(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Book_post(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

@api_view(['PUT'])
def Book_Put(request,pk):
    books = Books.objects.get(id=pk)
    serializer = BooksSerializer(instance=books,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def Book_delete(request,pk):
    books = Books.objects.get(id=pk)
    books.delete()
    return Response('Delete Successfully')