# Generated by Django 4.1.5 on 2023-01-15 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=32, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'tag',
            },
        ),
    ]
