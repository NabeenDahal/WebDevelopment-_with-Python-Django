# Generated by Django 3.2.12 on 2022-02-04 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('paragraph_1', models.TextField()),
                ('paragraph_2', models.TextField()),
                ('header_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('skill_1', models.CharField(max_length=150)),
                ('skill_2', models.CharField(max_length=150)),
                ('tools', models.CharField(max_length=150)),
            ],
        ),
    ]