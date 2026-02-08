from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    video = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "title", "description", "video"]

    def get_video(self, obj):
        # Return None if no video uploaded
        if not obj.video:
            return None
        
        # Return Cloudinary video URL with automatic format and quality
        try:
            return obj.video.build_url(
                resource_type="video",  # explicitly tell Cloudinary it's a video
                transformation=[
                    {"quality": "auto", "fetch_format": "auto"}
                ]
            )
        except Exception as e:
            # Catch any errors (e.g., invalid file) and return None
            return None


