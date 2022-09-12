# Generated by Django 3.2.5 on 2022-09-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistaprevia', '0009_auto_20220831_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.CharField(blank=True, default='0', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('En Stock', 'En Stock'), ('Sin Stock', 'Sin Stock'), ('Sin publicar', 'Sin publicar')], default='Sin publicar', max_length=15),
        ),
    ]
