from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import BookIndexPage
from wagtailmenus.models import FlatMenu, FlatMenuItem


@receiver(post_save, sender=BookIndexPage)
def create_menu(sender, instance, created, **kwargs):
    if created:
        try:
            menu = FlatMenu.objects.create(
                title=instance.title,
                handle=slugify(instance.title),
                site_id=2,
                max_levels=5,
            )
            instance.flat_menu = menu.handle
            instance.save()
            FlatMenuItem.objects.create(
                link_page_id=instance.pk, menu_id=menu.pk, allow_subnav=1
            )
        except:
            pass


# OtherModel.objects.create(something=kwargs['something'])
# YetAnotherModel.objects.create(
#     something_else=kwargs['something_else']
# )
