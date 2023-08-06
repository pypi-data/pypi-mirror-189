from django.db.models import BooleanField, CASCADE, CharField, ForeignKey, OneToOneField, PROTECT
from django.urls import reverse

from netbox.models import NetBoxModel
from ocp_project_plugin.choices import AppEnvironmentClusterEnvChoices


class OCPProject(NetBoxModel):
    name = CharField(
        max_length=255,
    )
    description = CharField(
        max_length=255,
    )
    display_name = CharField(
        max_length=255,
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
    )
    workload = CharField(
        max_length=255,
    )
    request = CharField(
        max_length=255,
    )

    clone_fields = ["name", "description", "display_name", "owner", "contact", "customer", "docu_url", "workload", "request"]

    class Meta:
        ordering = ["name", "description", "display_name", "owner", "contact", "customer", "docu_url", "workload", "request"]

    def __str__(self):
        return f"{self.name} ({self.display_name}-{self.customer})"

    def get_absolute_url(self):
        return reverse("plugins:ocp_project_plugin:ocpproject", kwargs={"pk": self.pk})

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/OCPProject/'


class AppEnvironment(NetBoxModel):
    cluster_env = CharField(
        max_length=3,
        choices=AppEnvironmentClusterEnvChoices,
        default=AppEnvironmentClusterEnvChoices.CHOICE_TST,
        verbose_name="Cluster ENV",
        help_text="The Cluster Environment",
    )
    app_env = CharField(
        max_length=20,
    )
    mtls = BooleanField()
    repo = CharField(
        max_length=255,
    )
    branch = CharField(
        max_length=20,
    )
    path = CharField(
        max_length=100,
    )
    egress_ip = CharField(
        max_length=20,
    )
    helm = BooleanField(
        default=False,
        verbose_name="HELM",
        help_text="Enable if helm should be used",
    )
    monitoring = BooleanField(
        default=False
    )
    postgres_monitoring = BooleanField(
        default=False
    )
    kustomize = BooleanField(
        default=False
    )
    requests_cpu = CharField(
        max_length=5,
        blank=False
    )
    requests_memory = CharField(
        max_length=5,
        blank=False
    )
    limits_cpu = CharField(
        max_length=5,
        blank=False
    )
    limits_memory = CharField(
        max_length=5,
        blank=False
    )
    ocp_project = ForeignKey(OCPProject, on_delete=CASCADE, related_name="app_env_ocp_project")

    clone_fields = ["cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                    "postgres_monitoring", "kustomize", "ocp_project", "requests_cpu", "requests_memory", "limits_cpu",
                    "limits_memory"]

    class Meta:
        ordering = ["cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "helm", "monitoring",
                    "postgres_monitoring", "kustomize", "ocp_project", "requests_cpu", "requests_memory", "limits_cpu",
                    "limits_memory"]

    def __str__(self):
        return f"{self.cluster_env}-{self.app_env} ({self.repo}-{self.branch})"

    def get_absolute_url(self):
        return reverse("plugins:ocp_project_plugin:appenvironment", kwargs={"pk": self.pk})

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/AppEnvironment/'


class ResourceQuota(NetBoxModel):
    requests_cpu = CharField(
        max_length=5,
    )
    requests_memory = CharField(
        max_length=5,
    )
    limits_cpu = CharField(
        max_length=5,
    )
    limits_memory = CharField(
        max_length=5,
    )
    app_environment = OneToOneField(
        AppEnvironment,
        on_delete=CASCADE,
        primary_key=True,
    )

    clone_fields = ["requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"]

    class Meta:
        ordering = ["requests_cpu", "requests_memory", "limits_cpu", "limits_memory", "app_environment"]

    def __str__(self):
        return f"{self.limits_cpu}/{self.limits_memory} ({self.requests_cpu}/{self.requests_memory})"

    def get_absolute_url(self):
        return reverse("plugins:ocp_project_plugin:resourcequota", kwargs={"pk": self.pk})

    @property
    def docs_url(self):
        return f'https://confluence.ti8m.ch/docs/models/ResourceQuota/'
