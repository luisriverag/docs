# Generated by Django 5.1.2 on 2024-12-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_activate_fuzzystrmatch_extension'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='depth',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='numchild',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='path',
            # Allow null values pending the next datamigration to populate the field
            field=models.CharField(db_collation='C', max_length=252, null=True, unique=True),
            preserve_default=False,
        ),
    ]
