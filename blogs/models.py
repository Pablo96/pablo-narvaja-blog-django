from django.db import models

"""
Tags are a way to filter the blogs.
They describe the blog content more precicely
and make searching for blogs easier.
"""
class Tag(models.Model):
    name=models.CharField(max_length=32, primary_key=True)

"""
A Blog represents an article in the site.
All fields are required.
"""
class Blog(models.Model):
    slug = models.SlugField(help_text='the id and url name of the blog', primary_key=True)
    title = models.CharField(max_length=128, null=False, blank=False)
    thumbnail_url = models.CharField(max_length=256, null=False, blank=False, help_text='the url to the image displayed in the blog list')
    description = models.CharField(max_length=256, null=False, blank=False)
    publish_date = models.DateTimeField(auto_now=True, null=False, blank=False)
    user_email = models.EmailField(help_text='email of the blog creator', null=False, blank=False)
    content_html = models.TextField()
    tags = models.ManyToManyField(to=Tag)

    def __str__(self) -> str:
        return "{\n\tslug:" + self.slug + "\n\ttitle:" + self.title + "\n}"
    
    class Meta:
        ordering = ['-publish_date']
        db_table = 'blog'

