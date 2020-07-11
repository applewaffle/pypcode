#!/usr/bin/env python
# Based on sleighexample.cc

import cppyy
import sys
import logging
import os.path
import platform

log = logging.getLogger(__name__)

PYPCODENATIVE_PATH = os.path.join(os.path.dirname(__file__), 'pypcode-native')
PYPCODENATIVE_LIBNAME = 'libpypcode-native'
SLEIGH_PATH = os.path.join(PYPCODENATIVE_PATH, 'sleigh-2.1.0')
SLEIGH_SRC_PATH = os.path.join(SLEIGH_PATH, 'src')
SLEIGH_SPECFILES_PATH = os.path.join(SLEIGH_PATH, 'specfiles')

# Determine shared library file extension
osname = platform.system()
if osname == 'Linux':
	PYPCODENATIVE_LIBNAME += '.so'
elif osname == 'Darwin':
	PYPCODENATIVE_LIBNAME += '.dylib'
elif osname == 'Windows':
	PYPCODENATIVE_LIBNAME += '.dll'
else:
	assert(False), "Unknown platform"

log.debug('Loading Library')
cppyy.include(os.path.join(PYPCODENATIVE_PATH, 'pypcode-native.h'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'translate.hh'))
cppyy.include(os.path.join(SLEIGH_SRC_PATH, 'error.hh'))
cppyy.load_library(os.path.join(PYPCODENATIVE_PATH, PYPCODENATIVE_LIBNAME))

class AssemblyEmitCacher(cppyy.gbl.AssemblyEmit):
  def dump(self, addr, mnem, body):
    self.addr = addr
    self.mnem = mnem
    self.body = body

# Import names into this namespace
from cppyy.gbl import Address
from cppyy.gbl import AddrSpace
from cppyy.gbl import ContextInternal
from cppyy.gbl import DocumentStorage
from cppyy.gbl import get_opname
from cppyy.gbl import PcodeRawOutHelper
from cppyy.gbl import SimpleLoadImage
from cppyy.gbl import Sleigh
from cppyy.gbl import OpCode
