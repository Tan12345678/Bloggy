# Generated by Django 4.2.5 on 2024-02-21 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_comment_created_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
