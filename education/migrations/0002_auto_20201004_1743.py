# Generated by Django 2.2.16 on 2020-10-04 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='testmark',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='storymark',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.EducationLevel'),
        ),
        migrations.AddField(
            model_name='storymark',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questresult',
            name='quest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.Quest'),
        ),
        migrations.AddField(
            model_name='questresult',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='questitem',
            name='quest',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.Quest'),
        ),
        migrations.AddField(
            model_name='questgroup',
            name='level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.EducationLevel'),
        ),
        migrations.AddField(
            model_name='quest',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.QuestGroup'),
        ),
        migrations.AddField(
            model_name='levelexamvariant',
            name='level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.LevelExam'),
        ),
        migrations.AddField(
            model_name='levelexammark',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.EducationLevel'),
        ),
        migrations.AddField(
            model_name='levelexammark',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='levelexam',
            name='level',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.EducationLevel'),
        ),
        migrations.AddField(
            model_name='igtvmark',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='education.EducationLevel'),
        ),
        migrations.AddField(
            model_name='igtvmark',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='grouptestvariant',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.GroupTest'),
        ),
        migrations.AddField(
            model_name='grouptest',
            name='group',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='education.QuestGroup'),
        ),
    ]
