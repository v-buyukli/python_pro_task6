from datetime import date

from django import forms
from django.core.exceptions import ValidationError


class TeacherForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=100)
    last_name = forms.CharField(label="Last name", max_length=100)
    patronymic = forms.CharField(label="Patronymic", max_length=100)
    birthdate = forms.DateField(label="Birthdate (yyyy-mm-dd)")
    subject = forms.CharField(label="Subject", max_length=100)

    @staticmethod
    def check_digits(string):
        return string.isalpha()

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if not TeacherForm.check_digits(first_name):
            raise ValidationError("Only letters are allowed for the First name...")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"]
        if not TeacherForm.check_digits(last_name):
            raise ValidationError("Only letters are allowed for the Last name...")
        return last_name

    def clean_patronymic(self):
        patronymic = self.cleaned_data["patronymic"]
        if not TeacherForm.check_digits(patronymic):
            raise ValidationError("Only letters are allowed for the Patronymic...")
        return patronymic

    def clean_birthdate(self):
        birthdate = self.cleaned_data["birthdate"]
        if birthdate > date(2003, 1, 1):
            raise ValidationError("The minimum age is 20 years (date < 2003-01-01)...")
        return birthdate

    def clean_subject(self):
        subject = self.cleaned_data["subject"]
        if not TeacherForm.check_digits(subject):
            raise ValidationError("Only letters are allowed for the Subject...")
        return subject


class GroupForm(forms.Form):
    group_name = forms.CharField(label="Group name", max_length=100)

    def clean_group_name(self):
        group_name = self.cleaned_data["group_name"]
        if not group_name[0].isalpha():
            raise ValidationError("Group name must start with a letter...")
        return group_name
