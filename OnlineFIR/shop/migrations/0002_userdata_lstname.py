# Generated by Django 2.2.5 on 2019-10-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='lstname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
