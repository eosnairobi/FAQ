from django.db import models
import uuid


def dapp_directory_path(instance, filename):
    # image will be uploaded to MEDIA_ROOT/dapps/>/profile/<filename>
    return 'dapps/{0}/{1}'.format(instance.name, filename)


def tool_directory_path(instance, filename):
    return 'tools/{}/{}'.format(instance.name, filename)


class DappCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=30, unique=True)


class ToolCategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)


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


class Tool(models.Model):
    name = models.CharField(max_length=30)
    created_by = models.CharField(max_length=50)
    link = models.URLField()
    creator_url = models.URLField()
    image = models.ImageField(upload_to=tool_directory_path)
    category = models.ForeignKey(ToolCategory, null=True, on_delete=models.SET_NULL)
