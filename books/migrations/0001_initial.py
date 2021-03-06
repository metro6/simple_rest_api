# Generated by Django 2.2.3 on 2019-07-09 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Book Name')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authors.Author')),
            ],
        ),
    ]
