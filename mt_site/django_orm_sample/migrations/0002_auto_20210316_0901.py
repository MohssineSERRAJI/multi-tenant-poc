# Generated by Django 3.1 on 2021-03-16 09:01

from django.db import migrations

from tenant_router.managers.tls import tls_tenant_manager


class DataLoader:
    initial_data = {
        "tenant-1.test.com": {
            "name": "Apollo hospitals",
            "address": "Chennai"
        },
        "tenant-2.test.com": {
            "name": "Fortis hospitals",
            "address": "Delhi"
        }
    }

    def load_data(self, apps, schema_editor):
        Hospital = apps.get_model('django_orm_sample', 'Hospital')
        tenant_id = tls_tenant_manager.current_tenant_context.id
        Hospital.objects.get_or_create(**self.initial_data[tenant_id])

    def unload_data(self, apps, schema_editor):
        Hospital = apps.get_model('django_orm_sample', 'Hospital')
        tenant_id = tls_tenant_manager.current_tenant_context.id

        qs = Hospital.objects.filter(
            name=self.initial_data[tenant_id]["name"]
        )

        if qs.exists():
            qs.delete()


data_loader = DataLoader()


class Migration(migrations.Migration):


    dependencies = [
        ('django_orm_sample', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            data_loader.load_data, reverse_code=data_loader.unload_data
        )
    ]

