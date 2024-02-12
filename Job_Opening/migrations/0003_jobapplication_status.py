# Generated by Django 4.1 on 2024-01-31 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Opening', '0002_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=1),
        ),
    ]
