#/usr/bin/python

from sympy import *
from optparse import OptionParser
from argparse import ArgumentParser
import os
import sys

def main(argv):

#----------argparse-----------------
	parser=ArgumentParser()
	parser.add_argument("--Kin","-T",action="store",dest="T",help="input should be the kinetic energy of the sysem"0)
	parser.add_argument("--Pot","-U",action="store",dest="U",help="input should be the potential energy of the sysem")

