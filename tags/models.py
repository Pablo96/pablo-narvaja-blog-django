from django.db import models

"""
Tags are a way to filter the blogs.
They describe the blog content more precicely
and make searching for blogs easier.
"""
class Tag(models.Model):
    name=models.CharField(max_length=32, primary_key=True)
    class Meta:
        db_table = 'tag'