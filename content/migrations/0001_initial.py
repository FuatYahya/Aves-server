# Generated by Django 3.2.6 on 2021-09-04 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.UUIDField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('size', models.BigIntegerField()),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('key', models.CharField(max_length=16)),
                ('nonce', models.CharField(max_length=12)),
                ('type', models.CharField(choices=[('Audio', 'Audio'), ('Video', 'Video')], max_length=25)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('tag', models.ManyToManyField(to='content.Tag')),
            ],
        ),
    ]