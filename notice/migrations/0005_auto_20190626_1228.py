# Generated by Django 2.2.2 on 2019-06-26 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_auto_20190626_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, help_text='간단한 설명문', max_length=100, verbose_name='DESCRIPTION'),
        ),
    ]
