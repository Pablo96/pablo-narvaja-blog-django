# Generated by Django 4.1.5 on 2023-01-14 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('slug', models.SlugField(help_text='the id and url name of the blog', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('thumbnail_url', models.CharField(help_text='the url to the image displayed in the blog list', max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('user_email', models.EmailField(help_text='email of the blog creator', max_length=254)),
                ('content_html', models.TextField()),
                ('tags', models.ManyToManyField(to='tags.tag')),
            ],
            options={
                'db_table': 'blog',
                'ordering': ['-publish_date'],
            },
        ),
    ]
