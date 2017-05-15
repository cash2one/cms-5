# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
# from cbbweb.service.cache_service import cache_site



class Command(BaseCommand):

    def handle(self, *args, **options):
        print("cache command start")
        # cache_site()
        print("pass")
        print("cache command end")



