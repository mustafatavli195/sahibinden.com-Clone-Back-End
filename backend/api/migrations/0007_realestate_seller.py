# Generated by Django 4.2.17 on 2024-12-07 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_realestate_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='realestate',
            name='seller',
            field=models.CharField(default='Owner', max_length=50),
        ),
    ]
