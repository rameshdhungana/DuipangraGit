# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-26 17:04
from __future__ import unicode_literals

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
            name='All',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_size', models.CharField(blank=True, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], help_text='this defines shirt size', max_length=40, null=True)),
                ('verbose_check', models.CharField(max_length=70, verbose_name='this is field to check verbose name')),
            ],
        ),
        migrations.CreateModel(
            name='all_and_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('all', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pangraall_and_userrelated', to='pangra.All')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inter_user', related_query_name='user_filter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bikeobject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
                ('image1', models.ImageField(default='hello', height_field=100, upload_to='image', width_field=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChildClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty', models.CharField(max_length=20)),
                ('digit', models.IntegerField()),
                ('dob', models.DateField()),
            ],
            options={
                'ordering': ['duty'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Specialuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pangraspecialuserrelated_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'hello sir',
                'ordering': ['post'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('article_piece', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pangra.Piece')),
            ],
            bases=('pangra.piece',),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_piece', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pangra.Piece')),
            ],
            bases=('pangra.piece',),
        ),
        migrations.CreateModel(
            name='Restuarent',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pangra.Place')),
                ('food', models.CharField(max_length=10)),
            ],
            bases=('pangra.place',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pangra.Place')),
                ('goods', models.CharField(max_length=68)),
            ],
            bases=('pangra.place',),
        ),
        migrations.AddField(
            model_name='all',
            name='user',
            field=models.ManyToManyField(through='pangra.all_and_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='proxyclass',
            fields=[
            ],
            options={
                'ordering': ['add'],
                'proxy': True,
            },
            bases=('pangra.place',),
        ),
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pangra.Article')),
                ('book_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pangra.Book')),
            ],
            bases=('pangra.book', 'pangra.article'),
        ),
        migrations.AddField(
            model_name='supplier',
            name='pasal',
            field=models.ManyToManyField(related_name='provider', to='pangra.Place'),
        ),
    ]
