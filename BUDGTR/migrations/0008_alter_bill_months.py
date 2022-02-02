# Generated by Django 4.0.1 on 2022-02-01 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BUDGTR', '0007_alter_bill_months'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='months',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='BUDGTR.month'),
        ),
    ]