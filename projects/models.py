import uuid

from django.db import models


class Project(models.Model):
    # owner
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    # feature_image
    demo_link = models.CharField(max_length=1000, blank=True, null=True)
    source_link = models.CharField(max_length=1000, blank=True, null=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYPES = (
        ('up', 'up'),
        ('down', 'down'),
    )
    # owner
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    value = models.CharField(max_length=100, choices=VOTE_TYPES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
