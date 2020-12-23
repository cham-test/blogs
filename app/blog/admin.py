from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Blog)


class PostModelAdmin(admin.ModelAdmin):
    model = Post

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(Post, PostModelAdmin)
