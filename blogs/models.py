from django.db import models

"""
A BlogPreview represents an article preview, meaning
it does not store the content of the blog, just the metadata
and the description. Used to list the blogs in the site.
All fields are required.
"""
class BlogPreview(models.Model):
    slug = models.SlugField(help_text='the id and url name of the blog', primary_key=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    thumbnail_url = models.CharField(max_length=256, null=False, blank=False, help_text='the url to the image displayed in the blog list')
    description = models.CharField(max_length=140, null=False, blank=False)
    publish_date = models.DateTimeField(null=False, blank=False)
    user_mail = models.EmailField(help_text='email of the blog creator', null=False, blank=False)

    def __str__(self) -> str:
        return "{\n\tslug:" + self.slug + "\n\ttitle:" + self.title + "\n}"
    
    class Meta:
        ordering = ['-publish_date']
        db_table = 'blog'


"""
A Blog represents full article in the site.
All fields are required
"""
class Blog(models.Model):
    preview = models.OneToOneField(
        BlogPreview,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    content_html = models.TextField()
    # Add tags

    def __str__(self) -> str:
        return "{\n\tslug:" + self.slug + "\n\ttitle:" + self.title + "\n}"
    
    class Meta:
        db_table = 'blog_content'