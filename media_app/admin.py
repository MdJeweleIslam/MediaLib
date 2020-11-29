from django.contrib import admin

# Register your models here.
from .models import Artist, VideoType, Songs, CastByArtish, Cast, Label, Video

admin.site.register(Artist)
admin.site.register(Video)
admin.site.register(VideoType)
admin.site.register(Songs)
admin.site.register(CastByArtish)
admin.site.register(Cast)
admin.site.register(Label)