# Generated by Django 4.1 on 2022-09-12 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0007_alter_post_age1_alter_post_age2"),
    ]

    operations = [
        migrations.RenameField(model_name="post", old_name="age2", new_name="max_age",),
        migrations.RenameField(model_name="post", old_name="age1", new_name="min_age",),
    ]
