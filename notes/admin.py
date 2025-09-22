from django.contrib import admin
from .models import Note, Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment

class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    inlines = [CommentInLine]

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'note', 'user', 'created_at']

admin.site.register(Note, NoteAdmin)
admin.site.register(Comment, CommentAdmin)