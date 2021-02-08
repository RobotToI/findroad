from django.db import models


class City(models.Model):
    # verbose par name give us a replaceword for our db-space
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        # There we also have option to change names which'll displayed
        ordering = ['name']
