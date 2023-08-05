# flake8: noqa
"""Script for adding lots of tasks to the queue for testing."""

import os
import sys
from pathlib import Path

myauth_dir = Path(__file__).parent.parent.parent.parent / "myauth"
sys.path.insert(0, str(myauth_dir))

import django
from django.apps import apps

# init and setup django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myauth.settings.local")
django.setup()

"""MAIN"""
from taskmonitor.core import celery_queues
from taskmonitor.tests.factories import QueuedTaskRawFactory

TASK_AMOUNT = 1_000

print(f"Started adding {TASK_AMOUNT:,} tasks to queued tasks...")
q_name = celery_queues.default_queue_name()
tasks = (QueuedTaskRawFactory() for _ in range(TASK_AMOUNT))
celery_queues.add_tasks(q_name, tasks)
print(f"Using queue name: {q_name}")
print(f"Added {TASK_AMOUNT:,} to queued tasks.")
