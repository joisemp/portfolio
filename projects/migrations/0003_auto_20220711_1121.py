# Generated by Django 3.2 on 2022-07-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_rename_programmingproject_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='link',
            new_name='primary_button_icon',
        ),
        migrations.AddField(
            model_name='project',
            name='bootstrap',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='figma',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='github',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='html',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='js',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='primary_button_text',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='primary_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='python',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='react',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='scss',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='secondary_button_icon',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='secondary_button_text',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='secondary_link',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
