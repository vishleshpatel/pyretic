
from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *

def main():
	forward1 = if_(match(srcip = '10.0.0.0/31'),fwd(1))
	return forward1

