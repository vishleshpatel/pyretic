from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *
import time
def main():
	
	list_srcIPs = []
	list_dstIPs = []
	with open('/home/vishlesh/SDN_RuleSetGenerator/SDN_RuleSetGenerator/matchedReachabilityPolicies.txt','r') as f:
		for line in f:
			(srcip,dstip_temp) = line.split(", ",1)
			dstip_temp = dstip_temp.split("(")
			DstIp = []
			for each_ip in dstip_temp:
				if not each_ip.find('.')==-1:
					each_ip = each_ip.split("'")	
					ip = each_ip[1]				
					DstIp.append(ip)
			list_srcIPs.append(srcip)
			list_dstIPs.append(DstIp)
	i=1
	##j=1 ##give some time to pyretic to install rules
	print(len(list_srcIPs))
	print(len(list_dstIPs))
	if(len(list_srcIPs) == len(list_dstIPs)):
		for srcip,dstip in zip(list_srcIPs,list_dstIPs):
			for each_ip in dstip:
				if i==1:
					i=i+1
					##j=j+1
					##forward = (match(srcip = str(srcip),dstip = str(each_ip)) >> fwd(i))
					notallowed = none
					notallowed = notallowed | match(srcip = str(srcip),dstip = str(each_ip))
				else:
					i=i+1
					##j=j+1
					notallowed = notallowed | match(srcip = str(srcip),dstip = str(each_ip))
					##forward = forward + (match(srcip = str(srcip),dstip = str(each_ip)) >> fwd(i))
					##if(i>250):
					##	print forward
					##	return forward
	print(notallowed)
	return notallowed

def isDestMatch(self,subnetAddrBig,subnetAddrSmall):
        set1 =([])
        prefix = subnetAddrBig._prefixlen
        subnetList = []
        while(prefix<=31):
            prefix = prefix+1
            subnetList = subnetAddrBig.subnets(new_prefix=prefix)
        set1 = set(subnetList)

        if subnetAddrSmall in set1:
            return True
        else:
            return False
