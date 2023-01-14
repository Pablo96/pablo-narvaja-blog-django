from django.db import models

"""
An AboutSection represents a HTML section in the about page.
The order is used to remember the order in which to display
the sections in the about page.
You can keep record of the about sections by just deactivating
them instead of deleting them.
"""
class AboutSection(models.Model):
    name = models.CharField(max_length=64, primary_key=True)
    title = models.CharField(max_length=256, null=False, blank=False)
    content = models.TextField()
    img_url = models.CharField(max_length=256, null=False, blank=False, help_text='the url to the image displayed in the about section')
    order = models.SmallIntegerField(null=False, unique=True)
    active = models.BooleanField(null=False, default=False)

    def __str__(self) -> str:
        return "{\n\tname:" + self.name + "\n\ttitle:" + self.title + "\n}"
    
    class Meta:
        db_table = 'about_section'

"""
The text of the footer section.
This is basically a unique instance 
but the design allows to keep a history of footers.
"""
class Footer(models.Model):
    id = models.AutoField(primary_key=True)
    content_html = models.TextField()

    def __str__(self) -> str:
        return "{\n\tname:" + self.name + "\n\ttitle:" + self.title + "\n}"
    
    class Meta:
        db_table = 'footer'
