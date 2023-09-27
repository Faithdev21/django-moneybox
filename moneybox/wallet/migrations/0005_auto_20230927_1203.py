# Generated by Django 3.2 on 2023-09-27 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20230917_0657'),
        ('wallet', '0004_auto_20230922_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currencyrate',
            options={'get_latest_by': ('created_at',), 'verbose_name': 'Currency rate', 'verbose_name_plural': 'Currency rates'},
        ),
        migrations.RemoveField(
            model_name='currencyrate',
            name='source_currency',
        ),
        migrations.RemoveField(
            model_name='currencyrate',
            name='target_currency',
        ),
        migrations.AddField(
            model_name='currencyrate',
            name='currency',
            field=models.ForeignKey(blank=True, help_text='Currency', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate', to='wallet.currency', verbose_name='Currency'),
        ),
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(db_index=True, help_text='Members of the group', related_name='groups', to='users.APIUser', verbose_name='Group members'),
        ),
    ]
