from django.shortcuts import redirect
from django.urls import reverse
from django_rq import get_queue, enqueue

import logging


def add_project(request):
    logger = logging.getLogger('netbox.ocp_project_plugin')

    try:
        enqueue("ocp_project_plugin.worker.pull_repository")
        logger.warning(f'Evaluating job started')
        return redirect(reverse('plugins:ocp_project_plugin:appenvironment_list'))
    except Exception as e:
        message = e
        logger.warning(f'{message}')
        return redirect(reverse('plugins:ocp_project_plugin:ocpproject_list'))


def clone_repo(request):
    logger = logging.getLogger('netbox.ocp_project_plugin')

    try:
        get_queue("default").enqueue("ocp_project_plugin.worker.clone_repository")
        logger.warning(f'Evaluating job started')
        return redirect(reverse('plugins:ocp_project_plugin:appenvironment_list'))
    except Exception as e:
        message = e
        logger.warning(f'{message}')
        return redirect(reverse('plugins:ocp_project_plugin:ocpproject_list'))


def sync_project(request):
    logger = logging.getLogger('netbox.ocp_project_plugin')

    logger.warning(f'{request}')
    get_queue("default").enqueue("ocp_project_plugin.worker.pull_repository")
    return redirect(reverse('plugins:ocp_project_plugin:ocpproject_list'))


