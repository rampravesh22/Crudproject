from django.shortcuts import render, HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User

# Create your views here.

# this function will add new item and show to the front user


def add_show(request):
    stud = User.objects.all()
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()

    return render(request, "enroll/addandshow.html", {"form": fm, "stu": stud})


# this function will edit or update data


def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, "enroll/updatestudent.html", {"form": fm, "stu": pi})


# this function will delete data from table


def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")

    return HttpResponseRedirect("")
