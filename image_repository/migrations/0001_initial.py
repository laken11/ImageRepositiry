# Generated by Django 3.1.5 on 2021-01-17 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=50, null=True, verbose_name='Information about the user uploading image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL, verbose_name='django user model object related to owner class')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='image name')),
                ('tag', models.CharField(default=models.CharField(max_length=20, verbose_name='image name'), max_length=20, verbose_name='tag on the image')),
                ('tag2', models.CharField(blank=True, max_length=20, null=True, verbose_name='tag on the image')),
                ('tag3', models.CharField(blank=True, max_length=20, null=True, verbose_name='tag on the image')),
                ('description', models.CharField(max_length=500, null=True, verbose_name='description of the image')),
                ('image', models.ImageField(upload_to='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='image_repository.owner', verbose_name='the owner of the image')),
            ],
        ),
    ]
