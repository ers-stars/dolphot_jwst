# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'DOLPHOT JWST'
copyright = '2022, 2023, 2024 Dan Weisz'
author = 'Weisz et al.'

release = '1.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

#templates_path = ['_templates']

# -- Options for HTML output

#extensions = [
#    ...
#    'sphinx_rtd_theme',
#]

html_theme = "sphinx_rtd_theme"

#html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
