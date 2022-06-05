# Generated by Django 2.2.5 on 2019-09-13 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0007_comment_published_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Avatar",
            fields=[
                ("id", models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name="ID"
                )
                 ),
                ("original_image", models.ImageField(
                    upload_to="",
                    verbose_name="Картинка, которую загружал "
                                 "пользователь (до 1200x1200)"
                )
                 ),
                ("profile_image", models.ImageField(
                    upload_to="",
                    verbose_name="Обрезанная картинка, которая "
                                 "отображается в профиле (200х400)"
                )
                 ),
                ("comment_image", models.ImageField(
                    upload_to="",
                    verbose_name="Обрезанная картинка, которая "
                                 "отображается в профиле (20х20)"
                )
                 ),
                ("user", models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL,
                    verbose_name="Пользователь"
                )
                 ),
            ],
        ),
    ]
