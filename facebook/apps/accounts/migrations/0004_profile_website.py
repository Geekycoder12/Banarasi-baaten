# Generated by Django 2.2.7 on 2019-11-18 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190928_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.URLField(blank=True, max_length=300, null=True),
        ),
    ]
