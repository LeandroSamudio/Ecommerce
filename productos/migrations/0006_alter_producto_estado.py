# Generated by Django 3.2.5 on 2022-11-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_alter_producto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.CharField(choices=[('En Stock', 'En Stock'), ('Sin Stock', 'Sin Stock'), ('Sin publicar', 'Sin publicar')], default='Publicado', max_length=15),
        ),
    ]
