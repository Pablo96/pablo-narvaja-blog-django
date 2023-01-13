# Generated by Django 4.1.5 on 2023-01-13 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPreview',
            fields=[
                ('slug', models.SlugField(help_text='the id and url name of the blog', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('thumbnail_url', models.CharField(help_text='the url to the image displayed in the blog list', max_length=256)),
                ('description', models.CharField(max_length=140)),
                ('publish_date', models.DateTimeField()),
                ('user_mail', models.EmailField(help_text='email of the blog creator', max_length=254)),
            ],
            options={
                'db_table': 'blog',
                'ordering': ['-publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('preview', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='blogs.blogpreview')),
                ('content_html', models.TextField()),
            ],
            options={
                'db_table': 'blog_content',
            },
        ),
    ]
