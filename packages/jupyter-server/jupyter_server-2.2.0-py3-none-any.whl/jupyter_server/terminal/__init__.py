"""Terminals support."""
import warnings

# Shims
from jupyter_server_terminals import api_handlers  # noqa
from jupyter_server_terminals.handlers import TermSocket  # noqa
from jupyter_server_terminals.terminalmanager import TerminalManager  # noqa

warnings.warn(
    "Terminals support has moved to `jupyter_server_terminals`",
    DeprecationWarning,
    stacklevel=2,
)


def initialize(webapp, root_dir, connection_url, settings):
    """Included for backward compat, but no-op."""
