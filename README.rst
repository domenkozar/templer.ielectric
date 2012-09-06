This is my personal collection of templates for Python development.

INSTALL
=======

::

    $ git clone https://github.com/iElectric/templer.ielectric.git
    $ cd templer.ielectric
    $ python bootstrap.py
    $ bin/buildout
    $ bin/templer <templatename> <output_directory>

Or::

    $ pip install templer.ielectric
    $ templer <templatename> <output_directory>

LIST OF TEMPLATES
=================

pyramid
    Opinionated Pyramid skeleton with:
    - Buildout staging/production configuration
    - SQLAlchemy integration
    - Alembic (database migrations)integration
    - Travis-CI integration
    - Jinja2 as default templating engine
    - Babel for internalization and localization
    - pyramid_mailer for sending emails
    - Raven (Sentry) integration
    - dogpile.cache for caching API
distribute_package
    Replaces paster's `basic_template` with more modern ideas :-)


TODO
====

- add bpython
- Pyramid template
    - maybe pyramid_layout?
    - alembic:
        - write tests
        - initial migration
    - docs how to use this package (http://docs.pylonsproject.org/projects/pyramid_mailer/en/latest/, )
    - pyramid_mailer # TODO: provide patch for printing mailer when in debug mode
    - http://dogpilecache.readthedocs.org/en/latest/
    - auth + root factory? https://github.com/lazaret/anuket/blob/develop/anuket/models/rootfactory.py 
    - fabric with staging/production deploy scripts
    - setup a way to detect locales/languages http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/i18n.html?awesome
    - local command to add new app for pyramid project
- add django template based on https://github.com/kiberpipa/intranet
- add plone template based on https://github.com/niteoweb/niteoweb.skel.plone
