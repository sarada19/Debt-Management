# Generated by Django 4.1 on 2022-08-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debt', '0006_debt_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_model',
            name='owed_by',
        ),
        migrations.RemoveField(
            model_name='user_model',
            name='owes',
        ),
        migrations.AddField(
            model_name='user_model',
            name='owed_by',
            field=models.ManyToManyField(null=True, to='debt.owed_by_model'),
        ),
        migrations.AddField(
            model_name='user_model',
            name='owes',
            field=models.ManyToManyField(null=True, to='debt.owes_model'),
        ),
    ]