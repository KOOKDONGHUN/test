# Generated by Django 2.2.3 on 2019-07-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldcup', '0006_auto_20190704_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityimage',
            name='image',
            field=models.ImageField(blank=True, default=500, upload_to=''),
        ),
        migrations.AlterField(
            model_name='enterimage',
            name='image',
            field=models.ImageField(blank=True, default=500, upload_to=''),
        ),
        migrations.AlterField(
            model_name='foodimage',
            name='image',
            field=models.ImageField(blank=True, default=500, upload_to=''),
        ),
        migrations.AlterField(
            model_name='movieimage',
            name='image',
            field=models.ImageField(blank=True, default=500, upload_to=''),
        ),
    ]