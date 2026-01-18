from django.shortcuts import render
from student.models import Student,Teacher


# Create your views here.
def home(request):
    all_data=Student.objects.all()
    all_data=Student.objects.filter(marks=89)
    all_data=Student.objects.exclude(city="Karachi")
    all_data=Student.objects.order_by("-city")
    all_data=Student.objects.order_by("?")
    all_data=Student.objects.order_by("name").reverse()
    all_data=Student.objects.order_by("name").reverse()[0:4]
    print("sql query:",all_data.query)
    all_data=Student.objects.values()
    all_data=Student.objects.values('name','roll')
    all_data=Student.objects.values_list('name','roll')
    all_data=Student.objects.values_list( named=True)
    print("all-data:",all_data)
    qs1=Student.objects.values_list('id','name',named=True)
    qs2=Teacher.objects.values_list('id','name',named=True)
    all_data=qs1.union(qs2,all=True)
    all_data=qs2.intersection(qs1)
    all_data=qs1.difference(qs2)
    print("all-data:",all_data)
    all_data=Student.objects.filter(marks=90)&Student.objects.filter(city="Karachi")
    all_data=Student.objects.filter(marks=90)|Student.objects.filter(city="Karachi")
    return render(request, 'student/home.html', {'all_data': all_data})