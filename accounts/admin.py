from django.contrib import admin
from django.utils.html import format_html
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "video_preview")
    readonly_fields = ("video_preview",)

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="300" controls>'
                '  <source src="{}" type="video/mp4">'
                'Your browser does not support the video tag.'
                '</video>',
                obj.video.url
            )
        return "No video"
    
    
