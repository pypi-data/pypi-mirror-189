import json
import uuid

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

from .core.celery_queues import QueuedTaskShort
from .helpers import extract_app_name
from .managers import QueuedTaskManager, TaskLogManager


class QueuedTask(models.Model):
    """A task that has been queued for later execution."""

    class Meta:
        managed = False

    app_name = models.CharField(max_length=255)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=255)
    priority = models.PositiveIntegerField(null=True, default=None)
    position = models.PositiveIntegerField()

    objects = QueuedTaskManager()

    def __str__(self):
        return self.id

    @classmethod
    def from_dict(cls, obj: dict, position: int) -> "QueuedTask":
        """Create object from dictionary (DEPRECATED)."""
        if "headers" not in obj:
            raise ValueError("headers missing in obj")
        headers = obj["headers"]
        properties = obj["properties"] if "properties" in obj else {}
        task_name = headers["task"]
        return cls(
            app_name=extract_app_name(task_name),
            id=headers["id"],
            name=task_name,
            priority=properties.get("priority"),
            position=position,
        )

    @classmethod
    def from_dto(cls, obj: QueuedTaskShort, position: int) -> "QueuedTask":
        """Create model object from data transport object."""
        return cls(
            app_name=obj.app_name,
            id=obj.id,
            name=obj.name,
            priority=obj.priority,
            position=position,
        )


class TaskReport(models.Model):
    """Dummy model to fake a 'Reports' entry on the admin index page."""

    class Meta:
        managed = False
        verbose_name = "report"

    id = models.BigIntegerField(primary_key=True)


class TaskLog(models.Model):
    """Log entry for an executed celery task."""

    class State(models.IntegerChoices):
        SUCCESS = 1, "success"
        RETRY = 2, "retry"
        FAILURE = 3, "failure"

    app_name = models.CharField(
        max_length=255, db_index=True, help_text="Name of the app this task belongs to."
    )
    args = models.JSONField(
        default=list,
        help_text=(
            "Positional arguments the task was called with. Nested items might be truncated to [] or {}."
        ),
    )
    exception = models.TextField(help_text="Message of the raised exception if any.")
    kwargs = models.JSONField(
        default=dict,
        help_text=(
            "Keyword arguments the task was called with. Nested items might be truncated to [] or {}."
        ),
    )
    parent_id = models.UUIDField(
        null=True, default=None, help_text="ID of the parent task if any."
    )
    priority = models.IntegerField(
        null=True, default=None, help_text="Priority this task was executed with."
    )
    result = models.JSONField(default=None, null=True, help_text="Result of the task.")
    retries = models.IntegerField(help_text="Number of retries.")
    received = models.DateTimeField(
        null=True,
        default=None,
        help_text="When a task is received from the broker and is ready for execution.",
    )
    runtime = models.FloatField(
        null=True,
        default=None,
        db_index=True,
        help_text="Runtime of this task in seconds.",
    )
    started = models.DateTimeField(
        null=True,
        default=None,
        help_text="When the task execution started.",
    )
    state = models.IntegerField(
        choices=State.choices,
        db_index=True,
        help_text="Task's state when it was logged.",
    )
    task_id = models.UUIDField(
        default=uuid.uuid4, db_index=True, help_text="Unique ID of this task."
    )
    task_name = models.CharField(
        max_length=255, db_index=True, help_text="Name of this task."
    )

    timestamp = models.DateTimeField(
        db_index=True, help_text="Timestamp when this log was created."
    )
    traceback = models.TextField(
        help_text="Full stack trace if there was an exception."
    )

    objects = TaskLogManager()

    def __str__(self):
        return f"{self.task_name}:{self.pk}"

    def save(self, *args, **kwargs) -> None:
        if self.started:
            self.runtime = (self.timestamp - self.started).total_seconds()
        super().save(*args, **kwargs)

    def asdict(self) -> dict:
        """Convert to representation as Python dict."""
        struct = {}
        for field in self._meta.fields:
            if field.choices:
                value = getattr(self, f"get_{field.name}_display")()
            else:
                value = getattr(self, field.name)
            # if callable(value):
            #     try:
            #         value = value() or ""
            #     except Exception:
            #         value = "Error retrieving value"
            if value is None:
                value = ""
            struct[field.name] = value
        return struct

    def asjson(self) -> str:
        """Convert to representation in JSON."""
        return json.dumps(
            self.asdict(), indent=4, sort_keys=True, cls=DjangoJSONEncoder
        )

    def astext(self) -> str:
        """Convert to text form that can be easily shared, e.g. on Discord chat."""
        text = "Task Log:"
        for key, value in self.asdict().items():
            text += "\n\n"
            if isinstance(value, (dict, list, tuple, set)) or key == "traceback":
                text += f"{key}:\n{value}"
            else:
                text += f"{key}: {value}"
        return text
