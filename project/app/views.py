from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

# Create your views here.
def home(request):
    data = Student.objects.create(Name="khushi",
                                   Email="Bhopal",
                                   Contact=9109558097,
                                    City="Bhopal")
    # data = Student.objects.first()
    data = Student.objects.last()
    # data = Student.objects.get(stu_name='name')
    # print(data.Name)
    # print(data.City)
    # print(data.Contact)
    # print(data.Email)
    return HttpResponse(data)
