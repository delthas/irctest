import subprocess

from irctest.basecontrollers import BaseClientController

class GircController(BaseClientController):
    def __init__(self):
        super().__init__()
        self.directory = None
        self.proc = None
    def __del__(self):
        if self.proc:
            self.proc.kill()
        if self.directory:
            self.directory.cleanup()

    def run(self, hostname, port, authentication):
        # Runs a client with the config given as arguments
        self.proc = subprocess.Popen(['girc_test', 'connect',
            '--host', hostname, '--port', str(port)])

def get_irctest_controller_class():
    return GircController