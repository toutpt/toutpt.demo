from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='toutpt.demo',
      version=version,
      description="a demo of my addons",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='jeanmichel.francois@makina-corpus.com',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['toutpt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          #addons
          'collective.googlenews',
          'collective.picnik',
          'collective.masonry',
          'collective.portlet.itemview',
          'collective.sugarcrm',
          'collective.gallery',
          'collective.googlelibraries',
          'collective.harlequin',
          'collective.hook',
          'collective.js.cufon',
          'collective.js.datatables',
          'collective.js.jqueryui',
          # -*- Extra requirements: -*-
          'plone.app.caching',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
