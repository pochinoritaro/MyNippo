# Generated by Django 5.1.4 on 2025-02-03 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(blank=True, default='', null=True, upload_to='icon/'),
        ),
    ]
