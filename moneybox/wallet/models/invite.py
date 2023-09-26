from django.utils import timezone

from wallet.models.timestamp import TimestampMixin

from django.db import models
from wallet.models.group import Group


class SafeDeletionMixin(models.Model):
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self):
        self.is_deleted = True
        self.save()

    def hard_delete(self):
        super().delete()


class Invite(TimestampMixin, SafeDeletionMixin):
    invite_code = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="invites")
    expires_at = models.DateTimeField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["invite_code", "group"], name="unique_invite"),
        ]
        verbose_name = "Invite"
        verbose_name_plural = "Invites"

    def is_expired(self):
        return self.expires_at < timezone.now()
