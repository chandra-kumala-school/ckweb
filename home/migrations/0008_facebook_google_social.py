# Generated by Django 2.2.8 on 2020-02-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_homepage_google_ad_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_tag', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Facebook site code',
                'verbose_name_plural': 'Facebook site code',
            },
        ),
        migrations.CreateModel(
            name='Google',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_tag', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Google site code',
                'verbose_name_plural': 'Google site code',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('css', models.CharField(blank=True, max_length=255, null=True, verbose_name='List CSS Classes (eg. text-primary py-0)')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Desc on hover (eg. December Bulletin)')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Link to resource (eg tel:+62-061-661-6765)')),
                ('icon', models.CharField(blank=True, max_length=255, null=True, verbose_name='FA Icon (eg. fas fa-newspaper fa-fw fa-2x)')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Visible text (eg. Latest School Bulletin)')),
            ],
            options={
                'verbose_name': 'Social Media link and icon',
                'verbose_name_plural': 'Social Media links and icons',
            },
        ),
    ]
