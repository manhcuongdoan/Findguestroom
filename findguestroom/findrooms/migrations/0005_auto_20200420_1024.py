# Generated by Django 3.0.5 on 2020-04-20 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findrooms', '0004_auto_20200420_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housead',
            name='livingroomImage',
            field=models.ImageField(upload_to='findrooms/media'),
        ),
    ]
