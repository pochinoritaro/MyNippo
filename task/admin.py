from django.contrib import admin
from task.models import Task


@admin.register(Task)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "document_url", "github_url", "is_public", "author", "get_members", "get_reviewers")
    search_fields = ("id",)

    def get_members(self, obj: Task):
        return ", ".join([user.username for user in obj.members.all()])

    def get_reviewers(self, obj: Task):
        return ", ".join([user.username for user in obj.reviewer.all()])

    get_members.short_description = "メンバー"
    get_reviewers.short_description = "レビュワー"
