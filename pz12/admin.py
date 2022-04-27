from django.contrib import admin

from pz12.models import Subjects, Teachers

# Register your models here.
@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    list_display = ('username', 'position', 'subject', 'cabinet', 'salary')


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'tcode', )