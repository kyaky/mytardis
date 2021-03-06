import shutil
from os import path
from tempfile import mkdtemp
from django.test import TestCase
from django.conf import settings
from django.contrib.staticfiles.management.commands import collectstatic


class CollectstaticTest(TestCase):

    def setUp(self):
        self.STATIC_ROOT = mkdtemp()
        self.cmd = collectstatic.Command()

    def tearDown(self):
        if path.exists(self.STATIC_ROOT):
            shutil.rmtree(self.STATIC_ROOT)

    def test_collectstatic(self):
        with self.settings(STATIC_ROOT=self.STATIC_ROOT, STATICFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage'):
            opts = {'interactive': False,
                    'verbosity': 0,
                    'link': False,
                    'clear': True,
                    'dry_run': False,
                    'ignore_patterns': [],
                    'use_default_ignore_patterns': True,
                    'post_process': True}
            self.cmd.handle(**opts)
