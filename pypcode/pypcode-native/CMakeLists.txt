cmake_minimum_required(VERSION 3.9)
project(pypcode-native)

if (MSVC)
    # warning level 4 and all warnings as errors
    # add_compile_options(/W4 /WX)
    add_compile_options(/O2)
else()
    # lots of warnings and all warnings as errors
    # add_compile_options(-Wall -Wextra -pedantic -Werror)
    add_compile_options(-O2 -Wall -Wno-sign-compare -D__TERMINAL__)
endif()

add_library(pypcode-native SHARED
	pypcode-native.cc

	# libsla sources
	sleigh-2.1.0/src/xml.cc
	sleigh-2.1.0/src/space.cc
	sleigh-2.1.0/src/float.cc
	sleigh-2.1.0/src/address.cc
	sleigh-2.1.0/src/pcoderaw.cc
	sleigh-2.1.0/src/translate.cc
	sleigh-2.1.0/src/opcodes.cc
	sleigh-2.1.0/src/globalcontext.cc
	sleigh-2.1.0/src/sleigh.cc
	sleigh-2.1.0/src/pcodeparse.cc
	sleigh-2.1.0/src/pcodecompile.cc
	sleigh-2.1.0/src/sleighbase.cc
	sleigh-2.1.0/src/slghsymbol.cc
	sleigh-2.1.0/src/slghpatexpress.cc
	sleigh-2.1.0/src/slghpattern.cc
	sleigh-2.1.0/src/semantics.cc
	sleigh-2.1.0/src/context.cc
	sleigh-2.1.0/src/filemanage.cc
	sleigh-2.1.0/src/loadimage.cc
	sleigh-2.1.0/src/memstate.cc
	sleigh-2.1.0/src/emulate.cc
	sleigh-2.1.0/src/opbehavior.cc
	)
