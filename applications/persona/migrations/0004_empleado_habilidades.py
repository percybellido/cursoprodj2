# Generated by Django 4.2.1 on 2023-05-25 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_habilidades_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidades'),
        ),
    ]
