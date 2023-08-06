from django.db.models import CharField, ForeignKey, PROTECT
from django.urls import reverse

from netbox.models import NetBoxModel
from ocp_project_plugin.models import AppEnvironment


class OCPProject(NetBoxModel):
    name = CharField(
        max_length=255,
        verbose_name="OCP Project Name",
        help_text="The ocp project name e.g. web-shop",
    )
    description = CharField(
        max_length=255,
        verbose_name="Description",
        help_text="The description of the project e.g. A web shop software",
    )
    display_name = CharField(
        max_length=255,
        verbose_name="Display name",
        help_text="Display Name of the project e.g. Web Shop Shopify"
    )
    owner = ForeignKey(
        to='tenancy.Contact',
        on_delete=PROTECT,
        related_name='ocp_project_owner',
    )
    contact = ForeignKey(
        to='tenancy.Contact',
        on_delete=PROTECT,
        related_name='ocp_project_contact',
    )
    customer = ForeignKey(
        to='tenancy.Tenant',
        on_delete=PROTECT,
        related_name='ocp_project_tenant',
    )
    docu_url = CharField(
        max_length=255,
        verbose_name="URL",
        help_text="The url of the project documentation e.g. https://confluence.com/space/project",
    )
    workload = CharField(
        max_length=255,
        verbose_name="Workload",
        help_text="The workload contents e.g. Postgres DB, nginx",
    )
    request = CharField(
        max_length=255,
        verbose_name="Jira Request",
        help_text="The jira request id e.g. TICKET1234",
    )

    clone_fields = ["name", "description", "display_name", "owner", "contact", "customer", "docu_url", "workload",
                    "request"]

    class Meta:
        ordering = ["name", "description", "display_name", "owner", "contact", "customer", "docu_url", "workload",
                    "request"]

    def __str__(self):
        return f"{self.name} ({self.display_name}-{self.customer})"

    def get_absolute_url(self):
        return reverse("plugins:ocp_project_plugin:ocpproject", kwargs={"pk": self.pk})

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/OCPProject/'

    def export_yaml_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'displayName': self.display_name,
            'customer': self.customer,
            'owner': self.owner,
            'contact': self.contact,
            'workloads': self.workload,
            'request': self.request,
            'url': self.docu_url
        }

    def count_app_environments(self):
        return AppEnvironment.objects.filter(OCPProject=self).count()

    def get_all_app_environments(self):
        return AppEnvironment.objects.filter(OCPProject=self)
