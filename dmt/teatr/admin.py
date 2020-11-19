from django.contrib import admin

from .models import Actor, Repertoire, RepertoirePhoto


class RepertoirePhotoInline(admin.TabularInline):
    model = RepertoirePhoto
    extra = 0


admin.site.register(Actor)

@admin.register(Repertoire)
class RepertoireAdmin(admin.ModelAdmin):
    inlines = [RepertoirePhotoInline]