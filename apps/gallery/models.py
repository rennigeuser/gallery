from django.db import models
from django.utils.translation import gettext as _
from shared.mixins.extra_information import CreatedAtUpdatedAtByMixin
from .functs import get_upload_path


class Post(CreatedAtUpdatedAtByMixin, models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Title')
    )
    icon = models.ForeignKey(
        'Image',
         on_delete=models.CASCADE,
         related_name='posts',
         verbose_name=_('Main icon')
    )
    icon_alt = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name=_('Image alternative name')
    )
    likes = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Amount of likes')
    )

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        ordering = ('likes', )

    def __str__(self):
        return self.title
    
    

class Image(models.Model):
    image = models.ImageField(
        upload_to=get_upload_path,
        verbose_name=_('Image')
    )

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return self.image.name



class Like(CreatedAtUpdatedAtByMixin, models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name=_("Post")
    )

    class Meta:
        verbose_name = _('Like')
        verbose_name_plural = _('Likes')
