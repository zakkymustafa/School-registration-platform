# Generated by Django 2.2.2 on 2019-10-03 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190704_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(null=True, to='course.Course'),
        ),
    ]
