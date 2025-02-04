from base import UUIDModelABC
from django.db import models
from account.models import User

class Task(UUIDModelABC):
    STATUS = (
        ("Draft", "下書き"),
        ("Todo", "下書き"),
        ("In Progress", "進行中"),
        ("Done", "完了"),
    )

    title = models.CharField(verbose_name="タイトル", max_length=30, blank=False, null=False)
    description = models.CharField(verbose_name="説明", max_length=255, blank=True, null=True)
    
    document_url = models.URLField(verbose_name="ドキュメントURL", blank=True, null=True)
    github_url = models.URLField(verbose_name="GitHubURL", blank=True, null=True)

    is_public = models.BooleanField(verbose_name="公開設定", default=True)
    
    #TODO Change "null=True" after insert data.
    author = models.ForeignKey(verbose_name="作成者", to=User, null=False, on_delete=models.PROTECT, related_name="tasks")
    reviewer = models.ManyToManyField(to=User, blank=True, related_name="review_tasks")
    members = models.ManyToManyField(to=User, blank=True, related_name="member_tasks")
    status = models.CharField(max_length=20, choices=STATUS, default="Draft")
    
    class Meta:
        db_table = "task"
        verbose_name = "タスク"
        verbose_name_plural = "タスク"
