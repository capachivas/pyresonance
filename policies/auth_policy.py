

from pyretic.lib.corelib import *
from pyretic.lib.std import *

from base_policy import *

class AuthPolicy_T(BasePolicy_T):
    
    def __init__(self, fsm):
        self.fsm = fsm
        
    def allow_policy(self):
        return passthrough
    
    def policy(self):
        # Match incoming flow with each state's flows
        match_auth_flows = self.fsm.get_policy('authenticated')
        
        # Create state policies for each state
        p1 = if_(match_auth_flows, self.allow_policy(), drop)

        # Parallel composition 
        return p1