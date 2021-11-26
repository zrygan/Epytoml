import os
import sys


#  EpyBake path
sys.path.insert(
    0,
    os.path.abspath(r"...\Epytoml\Epytoml"),
)

# Notaker path
sys.path.insert(
    0,
    os.path.abspath(r"...\Epytoml\Epytoml\Notaker"),
)


# information

project = "Epytoml"
copyright = "2021, Z1aaan"
author = "Z1aaan"
release = "1.0.2"


# configuration
extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
exclude_patterns = []
html_theme = "renku"
html_static_path = ["_static"]
