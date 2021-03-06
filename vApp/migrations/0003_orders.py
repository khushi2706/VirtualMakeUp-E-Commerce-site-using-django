# Generated by Django 3.1.4 on 2022-04-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vApp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=90)),
                ('email', models.CharField(default='', max_length=111)),
                ('address', models.CharField(default='', max_length=111)),
                ('city', models.CharField(default='', max_length=111)),
                ('state', models.CharField(default='', max_length=111)),
                ('amount', models.IntegerField(default=0)),
                ('zip_code', models.CharField(default='', max_length=111)),
                ('phone', models.CharField(default='', max_length=111)),
            ],
        ),
    ]
