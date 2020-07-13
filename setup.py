from setuptools import setup
from io import open
from ktorch_sphinx_theme import __version__

setup(
    name = 'ktorch_sphinx_theme',
    version =__version__,
    author = 'ktorch',
    author_email= 'meganset@gmail.com',
    url="https://github.com/ktorch/ktorch_sphinx_theme",
    docs_url="https://github.com/ktorch/ktorch_sphinx_theme",
    description='ktorch sphinx theme',
    py_modules = ['ktorch_sphinx_theme'],
    packages = ['ktorch_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'ktorch_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/fonts/*.*',
        'static/images/*.*',
        'theme_variables.jinja'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'ktorch_sphinx_theme = ktorch_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ]
)
