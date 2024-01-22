# Generated by Django 5.0.1 on 2024-01-21 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_transactions_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="u_id",
                to="app.users",
            ),
        ),
    ]