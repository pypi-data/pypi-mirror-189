# Generated by Django 3.0.4 on 2020-05-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kmuhelper', '0006_auto_20200428_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='bestellung',
            name='rechnung_gesendet',
            field=models.BooleanField(default=False, verbose_name='Rechnung gesendet'),
        ),
        migrations.AlterField(
            model_name='bestellung',
            name='zahlungsmethode',
            field=models.CharField(choices=[('bacs', 'Überweisung'), ('cheque', 'Scheck'), ('cod', 'Rechnung / Nachnahme'), ('paypal', 'PayPal')], default='cod', max_length=7, verbose_name='Zahlungsmethode'),
        ),
    ]
