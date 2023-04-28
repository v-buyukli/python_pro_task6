from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import TeacherForm
from .models import Teacher


def index(request):
    return HttpResponse("Hello. You're at the university index.")


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            Teacher.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                patronymic=request.POST["patronymic"],
                birthdate=request.POST["birthdate"],
                subject=request.POST["subject"],
            )
            return HttpResponseRedirect("/university/teachers")
    else:
        form = TeacherForm()
    return render(request, "teacher.html", {"form": form})


def show_teachers(request):
    teachers_list = list(Teacher.objects.all().values())
    context = {"teachers_list": teachers_list}
    return render(request, "teachers.html", context)


def add_group(request):
    pass


def show_groups(request):
    pass
