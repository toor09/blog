# Generated by Django 2.2.5 on 2019-09-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_auto_20190913_2109"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="image",
            field=models.ImageField(
                default="",
                upload_to="",
                verbose_name="Картинка для страницы этого тега"
            ),
            preserve_default=False,
        ),
    ]
