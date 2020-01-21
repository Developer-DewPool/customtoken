from __future__ import unicode_literals
from django.db import models
import uuid

class ApiUser(models.Model):
    email = models.EmailField(max_length=100, default='', blank=True)
    name = models.CharField(max_length=100, default='', blank=True)
    mobile_no = models.CharField(max_length=100, default='', blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)


class ApiKey(models.Model):
    user = models.ForeignKey(
        ApiUser, on_delete=models.CASCADE, related_name='user')
    hash_key = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    key = models.CharField(max_length=1000,  editable=False)
    active_status = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False):
        if ApiKey.objects.filter(user=self.user).exists():
            ApiKey.objects.filter(user=self.user).delete()

        self.key = 'maha_' + str(self.hash_key)
        super(ApiKey, self).save(force_insert, force_update)

    def __str__(self):
        return '{}'.format(self.user.name)
