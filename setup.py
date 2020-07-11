#!/usr/bin/env python
import os
import os.path
import platform
import shutil
import subprocess
from setuptools import setup
from setuptools.command.build_py import build_py

# SOURCE_DIR = os.path.abspath(os.path.dirname(__file__))
# LIB_SOURCE_DIR = os.path.join(SOURCE_DIR, 'pypcode', 'pypcode-native')
# OUTPUT_DIR = os.path.join(SOURCE_DIR, 'pypcode')

# class custom_build(build_py):
# 	def run(self):
# 		if not os.path.exists(OUTPUT_DIR):
# 			os.makedirs(OUTPUT_DIR)
# 		subprocess.check_call(['make'], cwd=LIB_SOURCE_DIR)
# 		shutil.copyfile(os.path.join(LIB_SOURCE_DIR, 'pypcode-native.so'),
# 		                os.path.join(OUTPUT_DIR,     'pypcode-native.so'))
# 		return super().run()


SOURCE_DIR = os.path.abspath(os.path.dirname(__file__))
LIB_SOURCE_DIR = os.path.join(SOURCE_DIR, 'pypcode', 'pypcode-native')
OUTPUT_DIR = os.path.join(SOURCE_DIR, 'pypcode', 'pypcode-native')

class custom_build(build_py):
	def run(self):
		try:
			out = subprocess.check_output(['cmake', '--version'])
		except OSError:
			raise RuntimeError('Please install CMake to build')

		cmake_args = [
			'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + OUTPUT_DIR,
			'-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON',
			'-DCMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE',
			'-DBUILD_SHARED_LIBS=TRUE'
			]
		# if platform.system() == 'Windows':
			# cmake_args += ['-G', 'MinGW Makefiles']
			# cmake_args += ['-DCMAKE_CXX_FLAGS="-D_WINDOWS=1 -D_WIN64=1"']
		if not os.path.exists(OUTPUT_DIR):
			os.makedirs(OUTPUT_DIR)
		subprocess.check_call(['cmake', '.'] + cmake_args, cwd=LIB_SOURCE_DIR)
		subprocess.check_call(['cmake', '--build', '.'], cwd=LIB_SOURCE_DIR)

		# Windows does things a little differently...
		win_lib_output = os.path.join(LIB_SOURCE_DIR, 'Debug', 'pypcode-native.dll')
		if platform.system() == 'Windows' and os.path.exists(win_lib_output):
			dest = os.path.join(OUTPUT_DIR, 'libpypcode-native.dll')
			shutil.copyfile(win_lib_output, dest)

		return super().run()


with open('README.md') as f:
	long_description = f.read()

setup(name='pypcode',
	version='0.0.1',
	description='Python bindings to Ghidra\'s SLEIGH library',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Matt Borgerson',
	author_email='contact@mborgerson.com',
	url='https://github.com/angr/pypcode',
	license='GPL',
	cmdclass=dict(build_py=custom_build),
	include_package_data=True,
	packages=['pypcode'],
	package_data={
		'pypcode': ['pypcode-native.*']
		},
	install_requires=[
		'cppyy'
		]
	)
