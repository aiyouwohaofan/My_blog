# Generated by Django 4.0.5 on 2022-06-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_views',
            field=models.PositiveIntegerField(default=0, verbose_name='文章访问量'),
        ),
    ]