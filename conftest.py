import pytest

from labgrid.protocol import CommandProtocol, ConsoleProtocol


@pytest.fixture(scope='session')
def command(target):
    shell = target.get_driver(CommandProtocol)
    target.activate(shell)
    return shell
"""    
@pytest.fixture(scope='session')
def cmd_line(target):
    shell = target.get_driver(ConsoleProtocol)
    target.activate(shell)
    return shell
    """
