# Generated by Django 4.1.4 on 2022-12-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_notice_category_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
    ]
