from django.db import models
from users.models import User
from django.utils.text import slugify


# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    code_block = models.TextField(max_length=None)
    language = models.CharField(max_length=100)
    user = models.ManyToManyField('users.User', related_name="user")
    tags = models.ManyToManyField('Tag', related_name="snippet_tag")

    def __str__(self):

        return f"Snippet title {self.title} Description {self.description} code block {self.code_block} language {self.language} tags {self.tags} user {self.user}"


class Tag(models.Model):
    name = models.CharField(max_length=40)
 # trying to add slug
    slug = models.SlugField(null=False, unique=True, default=slugify(name))

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
