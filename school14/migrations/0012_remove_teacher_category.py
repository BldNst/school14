# Generated by Django 4.2.11 on 2024-05-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school14', '0011_alter_teacher_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='category',
        ),
    ]
