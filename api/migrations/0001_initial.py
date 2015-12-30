# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField()),
                ('favorite', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='api.BaseModel')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100, null=True, blank=True)),
                ('label', models.CharField(max_length=100, null=True, blank=True)),
                ('released', models.DateField(null=True)),
            ],
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='api.BaseModel')),
                ('name', models.CharField(max_length=150)),
            ],
            bases=('api.basemodel',),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('basemodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='api.BaseModel')),
                ('title', models.CharField(max_length=150)),
                ('length', models.FloatField()),
                ('artist', models.ForeignKey(to='api.Artist')),
            ],
            bases=('api.basemodel',),
        ),
        migrations.AddField(
            model_name='basemodel',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='api.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(to='api.Song'),
        ),
    ]
