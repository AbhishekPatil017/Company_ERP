# Generated by Django 4.2.7 on 2023-11-22 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('particulars', models.CharField(blank=True, max_length=200, null=True)),
                ('company_name', models.CharField(blank=True, max_length=120, null=True)),
                ('company_gst', models.CharField(blank=True, max_length=120, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=30, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=120)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('customer_type', models.CharField(choices=[('intern', 'Intern'), ('client', 'Client')], max_length=120)),
                ('gst_number', models.CharField(blank=True, max_length=120, null=True)),
                ('particulars', models.CharField(blank=True, max_length=120, null=True)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('registered_date', models.DateField(auto_now_add=True)),
                ('joining_date', models.DateField()),
                ('duration', models.CharField(blank=True, max_length=120, null=True)),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('amount', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('gst_number', models.CharField(blank=True, max_length=120, null=True)),
                ('technology', models.CharField(blank=True, max_length=120, null=True)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('education', models.CharField(blank=True, max_length=120, null=True)),
                ('college', models.CharField(blank=True, max_length=120, null=True)),
                ('semester', models.CharField(blank=True, max_length=120, null=True)),
                ('aadharcard_no', models.CharField(blank=True, max_length=120, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=120, null=True)),
                ('email_id', models.CharField(blank=True, max_length=120, null=True)),
                ('registered_date', models.DateField(auto_now_add=True)),
                ('joining_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('amount', models.CharField(max_length=10)),
            ],
        ),
    ]