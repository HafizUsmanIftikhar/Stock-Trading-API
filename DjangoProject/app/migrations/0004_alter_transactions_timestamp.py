# Generated by Django 5.0.1 on 2024-01-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_transactions_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="timestamp",
            field=models.DateTimeField(default="2024-01-21 16:44"),
        ),
    ]
