# Generated by Django 5.1.4 on 2025-02-03 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_icon_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(null=True, upload_to='icon/'),
        ),
    ]
