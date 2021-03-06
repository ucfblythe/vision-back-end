# Generated by Django 2.1.3 on 2018-11-15 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisionUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, default='', max_length=255)),
                ('left', models.CharField(blank=True, default='', max_length=255)),
                ('right', models.CharField(blank=True, default='', max_length=255)),
                ('center', models.CharField(blank=True, default='', max_length=255)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
