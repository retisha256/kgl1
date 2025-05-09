# Generated by Django 5.2 on 2025-04-26 12:30

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProduceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_produce', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_produce', models.CharField(max_length=255)),
                ('date_and_time_of_produce', models.DateTimeField(auto_now_add=True)),
                ('tonnage', models.IntegerField()),
                ('cost', models.IntegerField(default=25)),
                ('name_of_dealer', models.CharField(max_length=255)),
                ('contact', models.CharField(default=20)),
                ('selling_price', models.IntegerField(blank=True, null=True)),
                ('current_stock', models.IntegerField(blank=True, null=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kglapp.branch')),
                ('type_of_produce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kglapp.producetype')),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_salesagent', models.BooleanField(default=False)),
                ('is_manager', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=25, unique=True)),
                ('email', models.EmailField(max_length=25, unique=True)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('phonenumber', models.CharField(blank=True, max_length=20)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='userprofile_groups', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='userprofile_permissions', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tonnage', models.IntegerField()),
                ('amount_paid', models.IntegerField(default=0)),
                ('buyers_name', models.CharField(max_length=35)),
                ('date_and_time', models.DateTimeField(auto_now_add=True)),
                ('is_sold_on_cash', models.BooleanField(default=False)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kglapp.branch')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kglapp.stock')),
                ('salesagent_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kglapp.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=255)),
                ('NIN', models.IntegerField(unique=True)),
                ('location', models.IntegerField(default=35)),
                ('contact', models.DateTimeField(default=20)),
                ('amount_due', models.IntegerField(default=False)),
                ('due_date', models.DateTimeField(auto_now_add=True)),
                ('tonnage', models.IntegerField()),
                ('Dispatch_date', models.DateTimeField(auto_now_add=True)),
                ('branch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kglapp.branch')),
                ('type_of_produce', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kglapp.producetype')),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kglapp.stock')),
                ('salesagent_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kglapp.userprofile')),
            ],
        ),
    ]
