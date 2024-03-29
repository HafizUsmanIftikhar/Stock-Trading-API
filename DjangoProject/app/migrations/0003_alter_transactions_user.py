# Generated by Django 5.0.1 on 2024-01-20 09:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_transactions_transaction_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="u",
                to="app.users",
            ),
        ),
    ]
