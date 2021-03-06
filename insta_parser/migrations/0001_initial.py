# Generated by Django 2.2.16 on 2020-10-04 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Igtv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='IgtvHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_tag', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='StoryHashtag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_tag', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('hash_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='insta_parser.StoryHashtag')),
                ('highlight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stories', to='insta_parser.Highlight')),
            ],
        ),
    ]
