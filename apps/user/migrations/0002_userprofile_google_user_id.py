# Generated by Django 2.0.5 on 2018-05-16 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='google_user_id',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
