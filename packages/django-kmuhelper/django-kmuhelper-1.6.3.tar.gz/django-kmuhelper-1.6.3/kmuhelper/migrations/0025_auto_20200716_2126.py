# Generated by Django 3.0.4 on 2020-07-16 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kmuhelper', '0024_auto_20200716_1714'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDoNotiz',
            new_name='Notiz',
        ),
        migrations.CreateModel(
            name='ToDoNotiz',
            fields=[
            ],
            options={
                'verbose_name': 'Notiz',
                'verbose_name_plural': 'Notizen',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('kmuhelper.notiz',),
        ),
        migrations.AlterModelOptions(
            name='notiz',
            options={'verbose_name': 'Notiz', 'verbose_name_plural': 'Notizen'},
        ),
        migrations.AlterModelOptions(
            name='todoversand',
            options={'verbose_name': 'Bestellung', 'verbose_name_plural': 'Bestellungen'},
        ),
        migrations.AlterModelOptions(
            name='todozahlungseingang',
            options={'verbose_name': 'Bestellung', 'verbose_name_plural': 'Bestellung'},
        ),
    ]
