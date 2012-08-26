This is my personal collection of templates for Python development.

INSTALL
=======

::

    $ git clone https://github.com/iElectric/templer.ielectric.git
    $ cd templer.ielectric
    $ python bootstrap.py
    $ bin/buildout
    $ bin/templer <templatename> <output_directory>


LIST OF TEMPLATES
=================

pyramid
    Opinionated Pyramid skeleton with Buildout staging/production, SQLAlchemy, Travis-CI, ...


TODO
====

- local command to add new app for pyramid project
- integrate sqlhelpers+alembic
- add setuptools structure based on nose-selecttests
- fabric with staging/production deploy scripts
- add django template based on https://github.com/kiberpipa/intranet
- add plone template based on https://github.com/niteoweb/niteoweb.skel.plone
