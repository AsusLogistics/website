# Generated by Django 3.2.9 on 2021-12-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsusLogistic', '0002_auto_20211214_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectpoint',
            old_name='county',
            new_name='county2',
        ),
        migrations.RenameField(
            model_name='collectpoint',
            old_name='postcode',
            new_name='email',
        ),
        migrations.AddField(
            model_name='collectpoint',
            name='first_name2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='collectpoint',
            name='last_name2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='collectpoint',
            name='postcode2',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
