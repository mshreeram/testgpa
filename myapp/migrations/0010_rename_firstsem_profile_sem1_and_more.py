# Generated by Django 4.2 on 2023-05-05 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_profile_eightsem_alter_profile_fifthsem_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='firstSem',
            new_name='Sem1',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='secondSem',
            new_name='Sem2',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='thirdSem',
            new_name='Sem3',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fourthSem',
            new_name='Sem4',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fifthSem',
            new_name='Sem5',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='sixthSem',
            new_name='Sem6',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='seventhSem',
            new_name='Sem7',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='eightSem',
            new_name='Sem8',
        ),
    ]
