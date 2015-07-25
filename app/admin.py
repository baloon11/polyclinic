# coding: utf-8
from django.forms import ModelForm
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from suit_ckeditor.widgets import CKEditorWidget
from app.models import Doctor, Reception


class ReceptionInline(TabularInline):
    model = Reception


class DoctorForm(ModelForm):
    class Meta:
        widgets = {
            'info': CKEditorWidget(editor_options={'startupFocus': True})
        }


class DoctorAdmin(ModelAdmin):
    form = DoctorForm
    inlines = [ReceptionInline,]


class ReceptionForm(ModelForm):
    class Meta:
        widgets = {
            'patient_info': CKEditorWidget(editor_options={'startupFocus': True})
        }


class ReceptionAdmin(ModelAdmin):
    form = ReceptionForm


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Reception,ReceptionAdmin)





