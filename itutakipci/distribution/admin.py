from django.contrib import admin
from .models import Distribution,Lecturer,Lecture,Comment,Semester
# Register your models here.

class DistributionAdmin(admin.ModelAdmin):
    list_display=('semester','lecturer','lecture','created_on')
    search_fields=('semester','lecturer','lecture','created_on')

class LecturerAdmin(admin.ModelAdmin):
     list_display=('lecturer','get_lectures')
     search_fields=('lecturer','lecture')
     prepopulated_fields = {'slug': ('lecturer',)}

class LectureAdmin(admin.ModelAdmin):
     list_display=('lecture',)
     search_fields=('lecture',)
     prepopulated_fields = {'slug': ('lecture',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=('comment','created_on','author',"pk")
    search_fields=['comment','created_on','author']

admin.site.register(Distribution,DistributionAdmin)
admin.site.register(Lecturer,LecturerAdmin)
admin.site.register(Lecture,LectureAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Semester)
