# Generated by Django 5.1.2 on 2024-10-26 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loan',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Acc_no', models.IntegerField(primary_key=True, serialize=False)),
                ('Dob', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Balance', models.FloatField(default=0)),
            ],
        ),
    ]
