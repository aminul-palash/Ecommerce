# Generated by Django 2.1.2 on 2018-11-29 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmanagement', '0002_auto_20181126_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktransactionmodel',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Refund', 'Refund'), ('Not Refund', 'Not Refund')], default='Pending', max_length=32),
        ),
    ]