from django.contrib import admin

from .models import Actor, Repertoire, RepertoirePhoto


class RepertoirePhotoInline(admin.TabularInline):
    model = RepertoirePhoto
    # exclude = ['thumbnail']
    extra = 0


admin.site.register(Actor)

@admin.register(Repertoire)
class RepertoireAdmin(admin.ModelAdmin):
    inlines = [RepertoirePhotoInline]
    # exclude = ['poster_thumbnail']