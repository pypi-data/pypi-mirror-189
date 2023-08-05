# Generated by Django 3.2.10 on 2022-03-11 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kmuhelper', '0079_auto_20220305_2322'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ToDoLagerbestand',
        ),
        migrations.DeleteModel(
            name='ToDoLieferung',
        ),
        migrations.DeleteModel(
            name='ToDoNotiz',
        ),
        migrations.DeleteModel(
            name='ToDoVersand',
        ),
        migrations.DeleteModel(
            name='ToDoZahlungseingang',
        ),
        migrations.CreateModel(
            name='App_Lagerbestand',
            fields=[
            ],
            options={
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkte',
                'proxy': True,
                'default_permissions': ('add', 'change', 'view'),
                'indexes': [],
                'constraints': [],
            },
            bases=('kmuhelper.produkt',),
        ),
        migrations.CreateModel(
            name='App_ToDo',
            fields=[
            ],
            options={
                'verbose_name': 'Notiz',
                'verbose_name_plural': 'Notizen',
                'proxy': True,
                'default_permissions': ('add', 'change', 'view'),
                'indexes': [],
                'constraints': [],
            },
            bases=('kmuhelper.notiz',),
        ),
        migrations.CreateModel(
            name='App_Warenausgang',
            fields=[
            ],
            options={
                'verbose_name': 'Bestellung',
                'verbose_name_plural': 'Bestellungen',
                'proxy': True,
                'default_permissions': ('add', 'change', 'view'),
                'indexes': [],
                'constraints': [],
            },
            bases=('kmuhelper.bestellung',),
        ),
        migrations.CreateModel(
            name='App_Wareneingang',
            fields=[
            ],
            options={
                'verbose_name': 'Lieferung',
                'verbose_name_plural': 'Lieferungen',
                'proxy': True,
                'default_permissions': ('add', 'change', 'view'),
                'indexes': [],
                'constraints': [],
            },
            bases=('kmuhelper.lieferung',),
        ),
        migrations.CreateModel(
            name='App_Zahlungseingang',
            fields=[
            ],
            options={
                'verbose_name': 'Bestellung',
                'verbose_name_plural': 'Bestellung',
                'proxy': True,
                'default_permissions': ('add', 'change', 'view'),
                'indexes': [],
                'constraints': [],
            },
            bases=('kmuhelper.bestellung',),
        ),
    ]
