from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import TeacherForm, GroupForm
from .models import Teacher, Group


def index(request):
    name = "university"
    return render(request, "index.html", {"name": name})


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
    return render(request, "teachers.html", {"teachers_list": teachers_list})


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            Group.objects.create(group_name=request.POST["group_name"])
            return HttpResponseRedirect("/university/groups")
    else:
        form = GroupForm()
    return render(request, "group.html", {"form": form})


def show_groups(request):
    groups_list = list(Group.objects.all().values())
    return render(request, "groups.html", {"groups_list": groups_list})
