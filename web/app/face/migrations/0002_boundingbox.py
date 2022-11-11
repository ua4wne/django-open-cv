# Generated by Django 4.1.3 on 2022-11-10 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('face', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoundingBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top', models.DecimalField(decimal_places=3, max_digits=5)),
                ('right', models.DecimalField(decimal_places=3, max_digits=5)),
                ('bottom', models.DecimalField(decimal_places=3, max_digits=5)),
                ('left', models.DecimalField(decimal_places=3, max_digits=5)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face.url')),
            ],
        ),
    ]
