# Generated by Django 3.2.6 on 2021-09-05 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_content_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='author',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='content',
            name='is_preview',
            field=models.BooleanField(default=False),
        ),
    ]
