# Generated by Django 3.1.6 on 2021-02-10 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo2', '0002_auto_20210210_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsmodel',
            name='newsid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
