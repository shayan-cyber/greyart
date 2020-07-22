# Generated by Django 2.2.7 on 2020-05-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200513_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='poem',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('image', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
