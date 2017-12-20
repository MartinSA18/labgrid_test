import attr
import fcntl
import logging
import os
import select
import shlex
import subprocess
import re

from labgrid.factory import target_factory
from labgrid.driver.common import Driver
from labgrid.driver import SerialDriver
from labgrid.driver.consoleexpectmixin import ConsoleExpectMixin
from labgrid.protocol import ConsoleProtocol, CommandProtocol
from labgrid.resource import SerialPort
from labgrid.util import Timeout, gen_marker, PtxExpect
from labgrid.step import step

@target_factory.reg_driver
@attr.s(cmp=False)
class GoshDriver(ConsoleExpectMixin, Driver, CommandProtocol, ConsoleProtocol):

    bindings = {"console": ConsoleProtocol}
    

    def __attr_post_init__(self):
        super().__attrs_post_init__()
        
        
    @Driver.check_active
    @step(args=['cmd'], result=True)
    def run(self, cmd, *, step):
        self.console.sendline(cmd)
        return
       
       
    @Driver.check_active
    @step(args=['cmd'], result=True)
    def run_check(self, cmd, *, step):
        self.console.sendline(cmd)
        return
        
            
        
    @Driver.check_active
    @step(args=['param'], result=True)
    def get_param_state(self, param, expstate: int, *, step):
    
        command = str("param get " + param)
        matchtrue = param + " = " + str(expstate)
        self.console.sendline(command)
        index, before, match, after = self.console.expect(bytes(matchtrue, 'utf-8'), timeout=1)
        
        result_str = ''.join(str(re.compile(str(match))))
        
        if result_str != "":
            return True
        else:
            return False  
        
    @step()
    def get_status(self):
        self.console.sendline('')
        index, before, match, after = self.console.expect(bytes(' #', 'utf-8'), timeout=1)
        
        result_str = ''.join(str(re.compile(str(index))))
        
        if result_str != "":
            return 1
        else:
            return 0
        
        return index
        
      
      
      
        
    @Driver.check_active
    @step(args=['cmd', 'pattern'])
    def wait_for(self, cmd, pattern, timeout=30.0, sleepduration=1):
        return
