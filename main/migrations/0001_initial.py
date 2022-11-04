# Generated by Django 4.1.3 on 2022-11-04 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_id', models.CharField(max_length=100)),
                ('store_name', models.TextField()),
                ('address', models.TextField()),
                ('menu', models.TextField()),
                ('star', models.TextField()),
                ('content', models.TextField(null=True)),
                ('img', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
