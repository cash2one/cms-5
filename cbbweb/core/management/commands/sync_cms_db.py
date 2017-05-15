# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand

from cbbweb.service.sync_cms_db_service import run_sync_cms_db




class Command(BaseCommand):

    def handle(self, *args, **options):

        run_sync_cms_db()


