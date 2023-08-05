"""
Run tox environments in sequential order.
"""
from __future__ import annotations

from tox.config.cli.parser import ToxParser
from tox.plugin import impl
from tox.session.state import State

from ...env_select import CliEnv, register_env_select_flags
from .common import env_run_create_flags, execute


@impl
def tox_add_option(parser: ToxParser) -> None:
    our = parser.add_command("run", ["r"], "run environments", run_sequential)
    register_env_select_flags(our, default=CliEnv())
    env_run_create_flags(our, mode="run")


def run_sequential(state: State) -> int:
    return execute(state, max_workers=1, has_spinner=False, live=True)
