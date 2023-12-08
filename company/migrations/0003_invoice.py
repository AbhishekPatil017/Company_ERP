# Generated by Django 4.2.7 on 2023-12-04 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_delete_client_delete_intern'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(default=0, max_length=10)),
                ('invoice_date', models.DateField(blank=True, null=True)),
                ('amount', models.CharField(blank=True, max_length=120, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.customer')),
            ],
        ),
    ]
