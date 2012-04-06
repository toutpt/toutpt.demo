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
        "Programming Language :: Python",
        ],
      keywords='',
      author='JeanMichel FRANCOIS aka toutpt',
      author_email='jeanmichel.francois@makina-corpus.com',
      url='https://github.com/toutpt/toutpt.demo',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['toutpt'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          #addons
          'collective.aviaryimageeditor',
          'collective.galleria',
          'collective.gallery',
          'collective.googleanalytics',
          'collective.googledocsviewer',
          'collective.googlelibraries',
          'collective.googlenews',
          'collective.harlequin',
          'collective.hook',
          'collective.js.cufon',
          'collective.js.datatables',
          'collective.js.jqueryui',
          'collective.masonry',
          'collective.oembed',
          'collective.picnik',
          'collective.portlet.embed',
          'collective.portlet.itemview',
          'collective.portlet.oembed',
          'collective.sugarcrm',
          'plonetheme.responsive1140',
          'plonetheme.toutpt',
          # -*- Extra requirements: -*-
          #'toutpt.unloading',
          'collective.addthis',
          'collective.disqus',
          'fourdigits.portlet.twitter',
          'webcouturier.dropdownmenu',
          'Products.LinguaPlone',
          'Products.PloneFormGen',
          'plone.app.discussion',
          'plone.app.theming',
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
