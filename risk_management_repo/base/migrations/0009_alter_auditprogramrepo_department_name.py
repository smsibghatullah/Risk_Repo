# Generated by Django 4.2.3 on 2023-07-05 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auditprogramrepo_department_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditprogramrepo',
            name='department_name',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='base.department'),
        ),
    ]
