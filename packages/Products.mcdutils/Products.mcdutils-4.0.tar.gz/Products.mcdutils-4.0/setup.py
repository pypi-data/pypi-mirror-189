from setuptools import find_packages
from setuptools import setup


readme = open('README.rst').read()
history = open('CHANGES.txt').read()
long_description = readme + '\n\n' + history

setup(name='Products.mcdutils',
      version='4.0',
      description=('A Zope product with memcached-backed ZCache and '
                   'Zope session implementations.'),
      long_description=long_description,
      classifiers=[
        'Development Status :: 6 - Mature',
        'Environment :: Web Environment',
        'Framework :: Zope',
        'Framework :: Zope :: 5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP :: Session',
      ],
      keywords='zope session memcache memcached Products',
      author='Tres Seaver and contributors',
      author_email='tseaver@palladion.com',
      maintainer='Jens Vagelpohl',
      maintainer_email='jens@dataflake.org',
      url='https://mcdutils.readthedocs.io',
      project_urls={
        'Documentation': 'https://mcdutils.readthedocs.io',
        'Issue Tracker': ('https://github.com/dataflake/Products.mcdutils'
                          '/issues'),
        'Sources': 'https://github.com/dataflake/Products.mcdutils',
      },
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      namespace_packages=['Products'],
      zip_safe=False,
      python_requires='>=3.7',
      install_requires=[
        'setuptools',
        'python-memcached',
        'Zope >= 5',
        ],
      extras_require={
        'docs': ['repoze.sphinx.autointerface', 'Sphinx'],
        },
      )
