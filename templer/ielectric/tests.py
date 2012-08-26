import unittest2 as unittest
import os
import tempfile
import shutil

from scripttest import TestFileEnvironment


class BaseTemplateTest(unittest.TestCase):

    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, self.tempdir)

        # docs http://pythonpaste.org/scripttest/
        self.env = TestFileEnvironment(os.path.join(self.tempdir,
                                                    'test-output'),
                                       ignore_hidden=False)

    def create_template(self):
        root_dir = os.path.join(os.path.dirname(__file__), '../', '../',)
        return self.env.run('%s/bin/paster create -t %s proj --no-interactive'
                            % (root_dir, self.template))


class PyramidTempalteTest(BaseTemplateTest):
    template = 'pyramid'

    def test_everything(self):
        result = self.create_template()
        # see:http://travis-ci.org/#!/iElectric/templer.ielectric/jobs/2242556
        created_files = set(result.files_created.keys()) - \
            set(['proj/src/proj.egg-info/paster_plugins.txt'])

        self.assertEqual(
            created_files,
            set([
                'proj',
                'proj/bootstrap.py',
                'proj/buildout.cfg',
                'proj/buildout.d',
                'proj/buildout.d/base.cfg',
                'proj/buildout.d/development.cfg',
                'proj/buildout.d/production.cfg',
                'proj/buildout.d/staging.cfg',
                'proj/buildout.d/versions.cfg',
                'proj/docs',
                'proj/docs/api.rst',
                'proj/docs/conf.py',
                'proj/docs/glossary.rst',
                'proj/docs/index.rst',
                'proj/docs/intro.rst',
                'proj/etc',
                'proj/etc/development.ini.in',
                'proj/etc/nginx.conf.in',
                'proj/etc/production.ini.in',
                'proj/.gitignore',
                'proj/HISTORY.rst',
                'proj/LICENSE',
                'proj/MANIFEST.in',
                'proj/.pep8',
                'proj/pre-commit-check.sh',
                'proj/README.rst',
                'proj/setup.cfg',
                'proj/setup.py',
                'proj/src',
                'proj/src/proj',
                'proj/src/proj.egg-info',
                'proj/src/proj.egg-info/dependency_links.txt',
                'proj/src/proj.egg-info/entry_points.txt',
                'proj/src/proj.egg-info/not-zip-safe',
                'proj/src/proj.egg-info/PKG-INFO',
                'proj/src/proj.egg-info/requires.txt',
                'proj/src/proj.egg-info/SOURCES.txt',
                'proj/src/proj.egg-info/top_level.txt',
                'proj/src/proj/__init__.py',
                'proj/src/proj/site',
                'proj/src/proj/site/__init__.py',
                'proj/src/proj/site/models.py',
                'proj/src/proj/site/static',
                'proj/src/proj/site/static/style.css',
                'proj/src/proj/site/templates',
                'proj/src/proj/site/templates/index.jinja2',
                'proj/src/proj/site/tests',
                'proj/src/proj/site/tests.py',
                'proj/src/proj/site/tests/__init__.py',
                'proj/src/proj/site/tests/test_views.py',
                'proj/src/proj/site/views.py',
                'proj/src/proj/testing.py',
                'proj/src/proj/tests.py',
                'proj/.travis.yml',
                ])
        )

        self.env.run('python bootstrap.py',
                     cwd=os.path.join(self.env.cwd, 'proj'),
                     expect_stderr=True)
        self.env.run('bin/buildout',
                     cwd=os.path.join(self.env.cwd, 'proj'),
                     expect_stderr=True)
        self.env.run('./pre-commit-check.sh',
                     cwd=os.path.join(self.env.cwd, 'proj'),
                     expect_stderr=True)


class DistributePackageTempalteTest(BaseTemplateTest):
    template = 'distribute_package'

    def test_everything(self):
        result = self.create_template()
        self.assertEqual(
            set(result.files_created.keys()),
            set([
                'proj',
                'proj/docs',
                'proj/.gitignore',
                'proj/HISTORY.rst',
                'proj/LICENSE',
                'proj/MANIFEST.in',
                'proj/.pep8',
                'proj/pre-commit-check.sh',
                'proj/proj',
                'proj/proj.egg-info',
                'proj/proj.egg-info/dependency_links.txt',
                'proj/proj.egg-info/entry_points.txt',
                'proj/proj.egg-info/not-zip-safe',
                'proj/proj.egg-info/PKG-INFO',
                'proj/proj.egg-info/requires.txt',
                'proj/proj.egg-info/SOURCES.txt',
                'proj/proj.egg-info/top_level.txt',
                'proj/proj/__init__.py',
                'proj/README.rst',
                'proj/setup.cfg',
                'proj/setup.py',
                'proj/.travis.yml',
                ]))
