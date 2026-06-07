from django.db import migrations


OLD_DEFAULT_LOGO = 'defaults/default_logo.jpg'
NEW_DEFAULT_LOGO = 'defaults/default_logo.png'
NEW_DEFAULT_WALLPAPER = 'defaults/default_wallpaper.svg'


def normalize_studio_default_images(apps, schema_editor):
    Studio = apps.get_model('games', 'Studio')

    for studio in Studio.objects.all():
        if not studio.logo or studio.logo.name == OLD_DEFAULT_LOGO:
            studio.logo = NEW_DEFAULT_LOGO

        if not studio.wallpaper:
            studio.wallpaper = NEW_DEFAULT_WALLPAPER

        studio.save(update_fields=['logo', 'wallpaper'])


def reverse_normalize_studio_default_images(apps, schema_editor):
    Studio = apps.get_model('games', 'Studio')

    for studio in Studio.objects.all():
        if studio.logo and studio.logo.name == NEW_DEFAULT_LOGO:
            studio.logo = OLD_DEFAULT_LOGO
        if studio.wallpaper and studio.wallpaper.name == NEW_DEFAULT_WALLPAPER:
            studio.wallpaper = ''

        studio.save(update_fields=['logo', 'wallpaper'])


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_alter_studio_logo_alter_studio_wallpaper'),
    ]

    operations = [
        migrations.RunPython(normalize_studio_default_images, reverse_normalize_studio_default_images),
    ]
