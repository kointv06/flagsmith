# Generated by Django 3.2.17 on 2023-02-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0053_delete_historical_feature_segment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='featurestate',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='featurestatevalue',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfeature',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfeaturestate',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfeaturestatevalue',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
    ]