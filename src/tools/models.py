from django.db import models
import uuid

STATUS_CHOICES = (
    ('LIVE', 'LIVE'),
    ('PENDING', 'PENDING'),
    ('UNDER_DEV', 'UNDER_DEV')
)


def dapp_directory_path(instance, filename):
    # image will be uploaded to MEDIA_ROOT/dapps/>/profile/<filename>
    return 'dapps/{0}/{1}'.format(instance.name, filename)


def tool_directory_path(instance, filename):
    return 'tools/{}/{}'.format(instance.name, filename)


class DappCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class ToolCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Dapp(models.Model):
    """A Dapp. Has name, creator, URL to creator, url to tool and URL
        to tool
    """

    name = models.CharField(max_length=30)
    created_by = models.CharField(max_length=50)
    link = models.URLField()
    creator_url = models.URLField()
    image = models.ImageField(upload_to=dapp_directory_path)
    category = models.ForeignKey(DappCategory, null=True, on_delete=models.SET_NULL)
    about = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=30)
    created_by = models.CharField(max_length=50)
    link = models.URLField()
    creator_url = models.URLField()
    image = models.ImageField(upload_to=tool_directory_path)
    category = models.ForeignKey(ToolCategory, null=True, on_delete=models.SET_NULL)
    about = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
