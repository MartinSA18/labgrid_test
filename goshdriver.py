import attr

from labgrid.factory import target_factory
from labgrid.driver.common import Driver
from labgrid.driver.consoleexpectmixin import ConsoleExpectMixin
from labgrid.protocol import ConsoleProtocol, CommandProtocol
from labgrid.resource import SerialPort
from labgrid.util import Timeout, gen_marker
from labgrid.step import step

@target_factory.reg_driver
@attr.s(cmp=False)
class GoshDriver(Driver, CommandProtocol):

    cmd = attr.ib(validator=attr.validators.instance_of(str))
    txdelay = attr.ib(default=0.0, validator=attr.validators.instance_of(float))


    bindings = {"console": ConsoleProtocol}
    

    def __attr_post_init__(self):
        super().__attr_post_init__()

        
    @Driver.check_active
    @step(args=['cmd'], result=True)
    def run(self, cmd, *, step):
        self.sendline(cmd)
        
        
    @Driver.check_active
    def run_check(self, cmd):
        return 

    @step()
    def get_status(self):
        return
        
        
    @Driver.check_active
    @step(args=['cmd', 'pattern'])
    def wait_for(self, cmd, pattern, timeout=30.0, sleepduration=1):
        return
