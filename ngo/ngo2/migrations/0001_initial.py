# Generated by Django 3.1.6 on 2021-02-09 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsphoto', models.ImageField(upload_to='myimage')),
                ('newscreatetime', models.DateTimeField(auto_now_add=True)),
                ('newstitle', models.CharField(max_length=200)),
                ('newspost', models.TextField()),
            ],
            options={
                'db_table': 'News',
            },
        ),
        migrations.CreateModel(
            name='Quotesmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotesphoto', models.ImageField(upload_to='myimage')),
                ('quotescreatetime', models.DateTimeField(auto_now_add=True)),
                ('quotestitle', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Quotes',
            },
        ),
        migrations.CreateModel(
            name='Tributemodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tributephoto', models.ImageField(upload_to='myimage')),
                ('tributecreatetime', models.DateTimeField(auto_now_add=True)),
                ('tributetitle', models.CharField(max_length=200)),
                ('tributepost', models.TextField()),
            ],
            options={
                'db_table': 'Tribute',
            },
        ),
    ]
