from django.db import models

"""
A Blog represents full article in the site.
All fields are required
"""
class Blog(models.Model):
    slug: models.SlugField(help_text='the id and url name of the blog', unique=True, null=False)
    title: models.CharField(max_length=100, null=False)
    thumbnail_url: models.CharField(max_length=256, null=False, help_text='the url to the image displayed in the blog list')
    description: models.CharField(max_length=140, null=False)
    publish_date: models.DateTimeField(auto_now_add=True, null=False)
    user_mail: models.EmailField(help_text='email of the blog creator', null=False)
    content_html: models.TextField()
    # Add tags

    def __str__(self) -> str:
        return "{\n\tslug:" + self.slug + "\n\ttitle:" + self.title + "\n}"


"""
A BlogPreview represents an article preview, meaning
it does not store the content of the blog, just the metadata
and the description. Used to list the blogs in the site.
All fields are required.
"""
class BlogPreview(models.Model):
    slug: models.SlugField(help_text='the id and url name of the blog', unique=True, null=False)
    title: models.CharField(max_length=100, null=False)
    thumbnail_url: models.CharField(max_length=256, null=False, help_text='the url to the image displayed in the blog list')
    description: models.CharField(max_length=140, null=False)
    publish_date: models.DateTimeField(auto_now_add=True, null=False)
    user_mail: models.EmailField(help_text='email of the blog creator', null=False)

    def __str__(self) -> str:
        return "{\n\tslug:" + self.slug + "\n\ttitle:" + self.title + "\n}"
    
    class Meta:
        ordering = ['-publish_date']
