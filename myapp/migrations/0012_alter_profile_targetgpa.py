# Generated by Django 4.2 on 2023-05-05 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_profile_sem1_alter_profile_sem2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='targetgpa',
            field=models.FloatField(default=0),
        ),
    ]
