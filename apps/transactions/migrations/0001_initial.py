# Generated by Django 4.2 on 2023-04-19 22:16

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('date_sale', models.DateField(blank=True, null=True)),
                ('discount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Replenishment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('date_buy', models.DateField(blank=True, null=True)),
                ('despesas', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('obs', models.CharField(blank=True, max_length=1055, null=True)),
                ('total', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=13, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
    ]