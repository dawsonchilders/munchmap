# Generated by Django 5.0.1 on 2024-02-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_restaurant_yelp_api_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='picture',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]