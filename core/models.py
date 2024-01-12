from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

NEWS = "News"
EVENTS = "Event"

POST = (
    (NEWS, "News"),
    (EVENTS, "Event"),
)

FIRST = "First"
SECOND = "Second"
THIRD = "Third"

SEMESTER = (
    (FIRST, "First"),
    (SECOND, "Second"),
    (THIRD, "Third"),
)


class NewsAndEventsQuerySet(models.query.QuerySet):
    def search(self, query):
        lookups = (
            Q(title__icontains=query)
            | Q(summary__icontains=query)
            | Q(posted_as__icontains=query)
        )
        return self.filter(lookups).distinct()


class NewsAndEventsManager(models.Manager):
    def get_queryset(self):
        return NewsAndEventsQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(
            id=id
        )  # NewsAndEvents.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().search(query)


class NewsAndEvents(models.Model):
    title = models.CharField(max_length=200, null=True)
    summary = models.TextField(max_length=200, blank=True, null=True)
    posted_as = models.CharField(choices=POST, max_length=10)
    updated_date = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    objects = NewsAndEventsManager()

    def __str__(self):
        return self.title


class Session(models.Model):
    session = models.CharField(max_length=200, unique=True)
    is_current_session = models.BooleanField(default=False, blank=True, null=True)
    next_session_begins = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.session


class Semester(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER, blank=True)
    is_current_semester = models.BooleanField(default=False, blank=True, null=True)
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, blank=True, null=True
    )
    next_semester_begins = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.semester


class ActivityLog(models.Model):
    """Keeps track of Creation, Update, and Deletion of records"""

    OPERATION_CHOICES = (
        ("C", "Creation"),
        ("U", "Update"),
        ("D", "Deletion"),
    )

    model_name = models.CharField(max_length=255)
    record_id = models.PositiveIntegerField(null=True, blank=True)
    record_name = models.CharField(max_length=255, null=True, blank=True)
    operation = models.CharField(max_length=1, choices=OPERATION_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.date}] {self.model_name}#{self.record_id} {self.record_name} {self.operation}"

    def get_human_readable_log(self):
        if self.operation == "C":
            name = f" with the name {self.record_name} " if self.record_name else ""
            return f"{self.model_name}{name}created"
        if self.operation == "U":
            name = f" with the name {self.record_name} " if self.record_name else ""
            return f"{self.model_name}[#{self.record_id}]{name}has been updated"
        if self.operation == "D":
            name = f" with the name {self.record_name} " if self.record_name else ""
            return f"{self.model_name}[#{self.record_id}]{name}has been deleted"

    @classmethod
    def log_save(cls, model, instance, name=None):
        """Helper to log the Creation or Update of a record"""
        cls.objects.create(
            model_name=model.__name__,
            record_id=instance.id if instance.id else None,
            record_name=name,
            operation="C" if not instance.id else "U",
        )

    @classmethod
    def log_delete(cls, model, instance, name=None):
        """Helper to log the Deletion of a record"""
        cls.objects.create(
            model_name=model.__name__,
            record_id=instance.id if instance.id else None,
            record_name=name,
            operation="D",
        )
