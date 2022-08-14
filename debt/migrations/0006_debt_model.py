# Generated by Django 4.1 on 2022-08-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debt', '0005_user_model_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lender', models.CharField(max_length=50)),
                ('borrower', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Debt List',
            },
        ),
    ]
