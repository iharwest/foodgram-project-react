from django.contrib import admin
from .models import Follow, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'email'
    )
    list_filter = ('email', 'username')
    search_fields = ('username',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author'
    )
    list_filter = ('user', 'author')
    search_fields = ('user__username', 'user__email')
