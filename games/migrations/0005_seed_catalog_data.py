from datetime import date

from django.db import migrations


NEW_STUDIOS = [
    {
        'name': 'Naughty Dog',
        'country': 'USA',
        'description': 'Story-driven studio known for cinematic action-adventure games.',
        'founding_year': 1984,
    },
    {
        'name': 'FromSoftware',
        'country': 'Japan',
        'description': 'Studio behind demanding action RPGs and atmospheric worlds.',
        'founding_year': 1986,
    },
    {
        'name': 'Larian Studios',
        'country': 'Belgium',
        'description': 'RPG studio focused on deep systems, choices, and co-op play.',
        'founding_year': 1996,
    },
    {
        'name': 'Rockstar Games',
        'country': 'USA',
        'description': 'Open-world studio famous for sprawling cinematic sandboxes.',
        'founding_year': 1998,
    },
    {
        'name': 'Ubisoft Montreal',
        'country': 'Canada',
        'description': 'Large-scale action studio behind stealth, adventure, and open-world hits.',
        'founding_year': 1997,
    },
    {
        'name': 'Creative Assembly',
        'country': 'United Kingdom',
        'description': 'Strategy studio known for grand campaigns and tactical battles.',
        'founding_year': 1987,
    },
    {
        'name': 'Supergiant Games',
        'country': 'USA',
        'description': 'Indie studio known for stylish, polished action games with strong art direction.',
        'founding_year': 2009,
    },
    {
        'name': 'Mojang Studios',
        'country': 'Sweden',
        'description': 'Sandbox and building-focused studio behind one of the most iconic games ever made.',
        'founding_year': 2009,
    },
    {
        'name': 'Insomniac Games',
        'country': 'USA',
        'description': 'Fast-paced action studio known for polished superhero and platforming games.',
        'founding_year': 1994,
    },
    {
        'name': 'BioWare',
        'country': 'Canada',
        'description': 'Narrative RPG studio focused on companions, choice, and epic worlds.',
        'founding_year': 1995,
    },
]

UPDATED_STUDIOS = [
    {
        'name': 'Valve',
        'country': 'USA',
        'description': 'A long-running PC studio known for groundbreaking first-person and puzzle games.',
        'founding_year': 1996,
    },
    {
        'name': 'Bethesda',
        'country': 'USA',
        'description': 'Open-world RPG studio famous for sprawling worlds and player freedom.',
        'founding_year': 1986,
    },
    {
        'name': 'CD Projekt',
        'country': 'Poland',
        'description': 'Studio behind story-rich RPGs and the GOG platform.',
        'founding_year': 1994,
    },
    {
        'name': 'id Software',
        'country': 'USA',
        'description': 'Legendary shooter studio that helped define the FPS genre.',
        'founding_year': 1991,
    },
]

NEW_GAMES = [
    {
        'title': 'The Last of Us Part I',
        'studio': 'Naughty Dog',
        'genre': 'Adventure',
        'release_date': date(2022, 9, 2),
        'platforms': ['PlayStation 5', 'Windows'],
    },
    {
        'title': 'Uncharted 4: A Thief\'s End',
        'studio': 'Naughty Dog',
        'genre': 'Adventure',
        'release_date': date(2016, 5, 10),
        'platforms': ['PlayStation 5', 'Windows'],
    },
    {
        'title': 'Elden Ring',
        'studio': 'FromSoftware',
        'genre': 'Action',
        'release_date': date(2022, 2, 25),
        'platforms': ['PlayStation 5', 'Windows', 'Xbox Series X/S'],
    },
    {
        'title': 'Sekiro: Shadows Die Twice',
        'studio': 'FromSoftware',
        'genre': 'Action',
        'release_date': date(2019, 3, 22),
        'platforms': ['Windows', 'PlayStation 5', 'Xbox Series X/S'],
    },
    {
        'title': 'Baldur\'s Gate 3',
        'studio': 'Larian Studios',
        'genre': 'RPG',
        'release_date': date(2023, 8, 3),
        'platforms': ['Windows', 'PlayStation 5'],
    },
    {
        'title': 'Divinity: Original Sin 2',
        'studio': 'Larian Studios',
        'genre': 'RPG',
        'release_date': date(2017, 9, 14),
        'platforms': ['Windows', 'PlayStation 5', 'Nintendo Switch'],
    },
    {
        'title': 'Grand Theft Auto V',
        'studio': 'Rockstar Games',
        'genre': 'Open World',
        'release_date': date(2013, 9, 17),
        'platforms': ['Windows', 'PlayStation 5', 'Xbox Series X/S'],
    },
    {
        'title': 'Red Dead Redemption 2',
        'studio': 'Rockstar Games',
        'genre': 'Open World',
        'release_date': date(2018, 10, 26),
        'platforms': ['Windows', 'PlayStation 5', 'Xbox Series X/S'],
    },
    {
        'title': 'Assassin\'s Creed Mirage',
        'studio': 'Ubisoft Montreal',
        'genre': 'Action',
        'release_date': date(2023, 10, 5),
        'platforms': ['Windows', 'PlayStation 5', 'Xbox Series X/S'],
    },
    {
        'title': 'Far Cry 6',
        'studio': 'Ubisoft Montreal',
        'genre': 'Shooter',
        'release_date': date(2021, 10, 7),
        'platforms': ['Windows', 'PlayStation 5', 'Xbox Series X/S'],
    },
    {
        'title': 'Total War: WARHAMMER III',
        'studio': 'Creative Assembly',
        'genre': 'Strategy',
        'release_date': date(2022, 2, 17),
        'platforms': ['Windows'],
    },
    {
        'title': 'Total War: Three Kingdoms',
        'studio': 'Creative Assembly',
        'genre': 'Strategy',
        'release_date': date(2019, 5, 23),
        'platforms': ['Windows'],
    },
    {
        'title': 'Hades',
        'studio': 'Supergiant Games',
        'genre': 'Action',
        'release_date': date(2020, 9, 17),
        'platforms': ['Windows', 'Nintendo Switch'],
    },
    {
        'title': 'Bastion',
        'studio': 'Supergiant Games',
        'genre': 'Action',
        'release_date': date(2011, 8, 16),
        'platforms': ['Windows', 'Nintendo Switch'],
    },
    {
        'title': 'Minecraft',
        'studio': 'Mojang Studios',
        'genre': 'Sandbox',
        'release_date': date(2011, 11, 18),
        'platforms': ['Windows', 'Nintendo Switch', 'Xbox Series X/S'],
    },
    {
        'title': 'Minecraft Legends',
        'studio': 'Mojang Studios',
        'genre': 'Strategy',
        'release_date': date(2023, 4, 18),
        'platforms': ['Windows', 'Nintendo Switch', 'Xbox Series X/S'],
    },
    {
        'title': 'Marvel\'s Spider-Man 2',
        'studio': 'Insomniac Games',
        'genre': 'Action',
        'release_date': date(2023, 10, 20),
        'platforms': ['PlayStation 5'],
    },
    {
        'title': 'Ratchet & Clank: Rift Apart',
        'studio': 'Insomniac Games',
        'genre': 'Action',
        'release_date': date(2021, 6, 11),
        'platforms': ['PlayStation 5', 'Windows'],
    },
    {
        'title': 'Dragon Age: Inquisition',
        'studio': 'BioWare',
        'genre': 'RPG',
        'release_date': date(2014, 11, 18),
        'platforms': ['Windows', 'PlayStation 5', 'Xbox Series X/S'],
    },
    {
        'title': 'Mass Effect Legendary Edition',
        'studio': 'BioWare',
        'genre': 'RPG',
        'release_date': date(2021, 5, 14),
        'platforms': ['Windows', 'PlayStation 5', 'Xbox Series X/S'],
    },
]


def seed_catalog(apps, schema_editor):
    Studio = apps.get_model('games', 'Studio')
    Game = apps.get_model('games', 'Game')
    Genre = apps.get_model('games', 'Genre')
    Platform = apps.get_model('games', 'Platform')

    genre_map = {}
    for genre_name in ['RPG', 'FPS', 'Strategy', 'Puzzle', 'Action', 'Adventure', 'Open World', 'Shooter', 'Sandbox']:
        genre, _ = Genre.objects.get_or_create(name=genre_name)
        genre_map[genre_name] = genre

    platform_map = {}
    for platform_name in ['Windows', 'Linux', 'macOS', 'PlayStation 5', 'Xbox Series X/S', 'Nintendo Switch']:
        platform, _ = Platform.objects.get_or_create(name=platform_name)
        platform_map[platform_name] = platform

    for studio_data in UPDATED_STUDIOS:
        Studio.objects.update_or_create(
            name=studio_data['name'],
            defaults={
                'country': studio_data['country'],
                'description': studio_data['description'],
                'founding_year': studio_data['founding_year'],
            },
        )

    for studio_data in NEW_STUDIOS:
        Studio.objects.update_or_create(
            name=studio_data['name'],
            defaults={
                'country': studio_data['country'],
                'description': studio_data['description'],
                'founding_year': studio_data['founding_year'],
            },
        )

    for game_data in NEW_GAMES:
        studio = Studio.objects.get(name=game_data['studio'])
        genre = genre_map[game_data['genre']]
        game, _ = Game.objects.update_or_create(
            title=game_data['title'],
            defaults={
                'studio': studio,
                'genre': genre,
                'release_date': game_data['release_date'],
                'description': f"{game_data['title']} is a catalog entry seeded for the library.",
            },
        )
        game.platforms.set([platform_map[name] for name in game_data['platforms']])


def unseed_catalog(apps, schema_editor):
    Game = apps.get_model('games', 'Game')
    Studio = apps.get_model('games', 'Studio')

    for title in [game['title'] for game in NEW_GAMES]:
        Game.objects.filter(title=title).delete()

    for name in [studio['name'] for studio in NEW_STUDIOS]:
        Studio.objects.filter(name=name).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_studio_description_studio_profile_picture_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_catalog, reverse_code=unseed_catalog),
    ]
