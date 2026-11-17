from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=160)
    description = models.TextField()
    icon = models.CharField(
        max_length=30,
        default='wrench',
        help_text='Icon name used on the website, e.g. wrench, armchair, paint-roller.',
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Untick to hide this service from the website without deleting it.',
    )
    display_order = models.PositiveSmallIntegerField(
        default=0, help_text='Lower numbers appear first.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return self.name