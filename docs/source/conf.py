# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Test Smells Catalog'
copyright = '2023, EASY'
author = 'Engineering and Systems Software Research Group\n - Universidade Federal de Alagoas (UFAL)'

release = '2.0'
version = '2.3.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_design'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_js_files = [
    'https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.1/jquery.min.js',
    '_static/flyout.js'
]

html_static_path = ['_static']
html_logo = "https://easy-group.netlify.app/img/easy.svg"
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

# rst_prolog = """

# .. |code_example| image:: https://github.com/easy-software-ufal/catalog-test-smells/blob/main/docs/source/_static/logo_example.png?raw=true
#         :alt: Code Example
#         :height: 25px

# .. |cause_effect| image:: https://github.com/easy-software-ufal/catalog-test-smells/blob/main/docs/source/_static/logo_causes_effects.png?raw=true
#         :alt: Cause and Effect
#         :height: 25px

# .. |freq| image:: https://github.com/easy-software-ufal/catalog-test-smells/blob/main/docs/source/_static/logo_freq.png?raw=true
#         :alt: Frequency
#         :height: 25px
# """
# -- Options for EPUB output
epub_show_urls = 'footnote'
