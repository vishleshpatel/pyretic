
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *

def main():

	
	forward1 =(match(srcip = '10.0.0.0/31')|match(srcip = '10.0.0.4/31'))>>fwd(1)
	##forward1 = forward1+(match(srcip = '10.0.0.4/31')>>fwd(2))

	return forward1

