import logging

from django_rq import job, get_queue
from dcim.models import Device
#from ocp_project_plugin.models import AppEnvironment, OCPProject, Collection, Compliance, ServiceMapping
from datetime import datetime
import time
#from ocp_project_plugin.choices import CollectFailChoices, CollectStatusChoices
import ipaddress
#from .ocp_project_plugincollect import CollectDeviceData
#from .ocp_project_plugincustom_exceptions import CollectionException
from django.db.models import Q
from git import Repo
#from ocp_project_plugin.choices import ServiceComplianceChoices
#from ocp_project_plugin.git_manager import get_device_config, get_days_after_update
#from ocp_project_plugin.config_manager import get_config_diff
from django.conf import settings

from .utils.gitlab import pull_repo
#import git
import os
import yaml
from yaml import SafeLoader
from collections import namedtuple

PLUGIN_SETTINGS = settings.PLUGINS_CONFIG.get('ocp_project_plugin', dict())
GITLAB_PROJECT_URL = PLUGIN_SETTINGS.get('gitlab_project_url', '')
VALUES_PATH = PLUGIN_SETTINGS.get('jira_browse_url', '')

"""
1. Git Repo pullen
2. Überprüfen ob es einen Branch mit dem Ticket Namen schon gibt
3. Neuer Branch erstellen mit dem Ticket Namen
4. Secrets entschlüsseln
5. OCPPRoject/AppEnvironment Model Daten in yaml konvertieren
6. YAML Daten dem values.yaml anfügen
7. Secrets der Secrets Datei anfügen
8. Secret verschlüsseln
9. Mergen
"""


@job("default")
def archive_pull_repository():
    #g = git.cmd.Git('/repo/project_repo')
    #result = g.pull()
    #print(f'{g.working_dir}-{result}')
    print()


@job("default")
def archive_clone_repository():
    logger = logging.getLogger('netbox.ocp_project_plugin')
    logger.warning(f'Started cloning')
    logger.warning(f'{GITLAB_PROJECT_URL}')
    #git.Git('/repo/').clone(GITLAB_PROJECT_URL)
    logger.warning(f'cloning finished')


@job("default")
def pull_repository():
    print("1. Git Repo pullen")
    get_queue("default").enqueue("ocp_project_plugin.worker.check_branch_existence")


@job("default")
def check_branch_existence():
    print("2. Überprüfen ob es einen Branch mit dem Ticket Namen schon gibt")
    get_queue("default").enqueue("ocp_project_plugin.worker.new_branch")


@job("default")
def new_branch():
    print("3. Neuer Branch erstellen mit dem Ticket Namen")
    get_queue("default").enqueue("ocp_project_plugin.worker.decrypt_secrets")


@job("default")
def decrypt_secrets():
    print("4. Secrets entschlüsseln")
    get_queue("default").enqueue("ocp_project_plugin.worker.convert_models_to_yaml")


@job("default")
def convert_models_to_yaml():
    print("5. OCPPRoject/AppEnvironment Model Daten in yaml konvertieren")
    get_queue("default").enqueue("ocp_project_plugin.worker.add_data_to_yaml")


@job("default")
def add_data_to_yaml():
    print("6. YAML Daten dem values.yaml anfügen")
    get_queue("default").enqueue("ocp_project_plugin.worker.add_secrets_to_yaml")


@job("default")
def add_secrets_to_yaml():
    print("7. Secrets der Secrets Datei anfügen")
    get_queue("default").enqueue("ocp_project_plugin.worker.encrypt_secrets")


@job("default")
def encrypt_secrets():
    print("8. Secret verschlüsseln")
    get_queue("default").enqueue("ocp_project_plugin.worker.merge_branch_to_main")


@job("default")
def merge_branch_to_main():
    print("9. Mergen")
