# Generated by Django 2.2.9 on 2019-12-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(default='')),
                ('clicks', models.IntegerField(default=0)),
                ('short_url', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Url',
                'verbose_name_plural': 'Urls',
            },
        ),
    ]