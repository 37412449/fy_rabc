# !/usr/bin/env python
# -*- coding: UTF-8 –*-

from django.contrib.admin.models import ADDITION, LogEntry
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.contenttypes.models import ContentType

ADDITION = 1
CHANGE = 2
DELETION = 3

ACTION_FLAG_CHOICES = (
    (ADDITION, _('Addition')),
    (CHANGE, _('Change')),
    (DELETION, _('Deletion')),
)


def get_content_type_for_model(obj):
    # Since this module gets imported in the application's root package,
    # it cannot import models from other applications at the module level.

    return ContentType.objects.get_for_model(obj, for_concrete_model=False)


class AdminLog:
    def __init__(self):
        pass

    def log_addition(self, request, object, message):
        """
        Log that an object has been successfully added.

        The default implementation creates an admin LogEntry object.
        """

        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=ADDITION,
            change_message=message,
        )

    def log_change(self, request, object, message):
        """
        Log that an object has been successfully changed.

        The default implementation creates an admin LogEntry object.
        """
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=str(object),
            action_flag=CHANGE,
            change_message=message,
        )

    def log_deletion(self, request, object, object_repr):
        """
        Log that an object will be deleted. Note that this method must be
        called before the deletion.

        The default implementation creates an admin LogEntry object.
        """
        return LogEntry.objects.log_action(
            user_id=request.user.pk,
            content_type_id=get_content_type_for_model(object).pk,
            object_id=object.pk,
            object_repr=object_repr,
            action_flag=DELETION,
        )
