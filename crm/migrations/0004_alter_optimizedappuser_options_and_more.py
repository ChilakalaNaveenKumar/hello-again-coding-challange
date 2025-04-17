# Generated by Django 5.2 on 2025-04-17 02:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crm", "0003_alter_customerrelationship_appuser"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="optimizedappuser",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="customerrelationship",
            name="appuser",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customerrelationships",
                to="crm.appuser",
            ),
        ),
        migrations.AlterField(
            model_name="optimizedcustomerrelationship",
            name="appuser",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customerrelationships",
                to="crm.optimizedappuser",
            ),
        ),
    ]
