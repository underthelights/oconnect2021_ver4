# Generated by Django 3.2.4 on 2021-06-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_news_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='link',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='LINK'),
        ),
    ]
