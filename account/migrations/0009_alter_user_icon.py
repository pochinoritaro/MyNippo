# Generated by Django 5.1.4 on 2025-02-04 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, default='icon/example.png', null=True, upload_to='account/icon/'),
        ),
    ]
