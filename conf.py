project="ИРС документы (master: 24.04.2023 13:37)"
author="ИРС"
copyright="2022 ИРС документы"
extensions = [
    'myst_parser',
    'sphinx_tabs.tabs',
    'sphinx_copybutton',
]
sphinx_tabs_disable_tab_closing = True
myst_enable_extensions = [
    'substitution',
]
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
source_suffix = {
    '.md': 'markdown',
    '.rst': 'restructuredtext',
}
html_static_path = ['_static_local']
html_style = 'css/custom.css'
html_js_files = [
    'js/custom.js'
]

root_doc="service.index"