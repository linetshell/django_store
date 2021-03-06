# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20140907_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'pic_folder/no-img.png', upload_to=b'pic_folder/', null=True, verbose_name=b'Image', blank=True),
        ),
    ]
