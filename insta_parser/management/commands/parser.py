import instaloader
from django.core.management.base import BaseCommand

from insta_parser.models import IgtvHashtag, Igtv
from main.models import MusicOneUser, STUDENT


def get_students_data():
    return MusicOneUser.objects.filter(role=STUDENT).values()


def get_igtv_hashtags():
    return IgtvHashtag.objects.all().values()


class Command(BaseCommand):

    def handle(self, *args, **options):
        students = get_students_data()
        igtv_hashtags = get_igtv_hashtags()
        for student in students:
            instagram = student['instagram']
            if 'alexmusic12321' not in instagram:
                continue

            instance = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(instance.context, username=instagram.split('/')[-2])

            for igtv_post in profile.get_igtv_posts():
                description = f'{igtv_post.caption} '
                for igtv_hashtag in igtv_hashtags:
                    hash_tag = igtv_hashtag['hash_tag']
                    if f'{hash_tag} ' in description:
                        igtv = Igtv(
                            hash_tag=IgtvHashtag.objects.get(hash_tag=hash_tag),
                            url=igtv_post.video_url,
                            user=MusicOneUser.objects.get(instagram=instagram),
                        )
                        igtv.save()
