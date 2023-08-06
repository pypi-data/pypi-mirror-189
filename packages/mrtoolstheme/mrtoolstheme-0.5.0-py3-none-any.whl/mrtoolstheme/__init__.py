"""Register the Sphinx HTML Theme `mrtools`.

.. moduleauthor:: Michael Rippstein <info@anatas.ch>

:copyright: Copyright 2022 by Michael Rippstein.
:license: AGPL, see LICENSE for details.
"""

from os import path


def setup(app):
    """Register the Sphinx HTML Theme `mrtools`."""
    app.add_html_theme('mrtools', path.abspath(path.dirname(__file__)))
