from django.db import models


class Response(models.Model):
    response = models.BooleanField()
    reason = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{'Accepted' if self.response else 'Declined'}"
