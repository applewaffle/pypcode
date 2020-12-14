
add_library(sla STATIC
    xml.cc
    space.cc
    float.cc
    address.cc
    pcoderaw.cc
    translate.cc
    opcodes.cc
    globalcontext.cc
    sleigh.cc
    pcodeparse.cc
    pcodecompile.cc
    sleighbase.cc
    slghsymbol.cc
    slghpatexpress.cc
    slghpattern.cc
    semantics.cc
    context.cc
    filemanage.cc
    loadimage.cc
    memstate.cc
    emulate.cc
    opbehavior.cc
)
#add_library(retdec::capstone2llvmir ALIAS capstone2llvmir)

target_compile_features(sla PRIVATE cxx_std_11)

target_compile_options(sla PRIVATE
                        -Wall 
                        -Wno-sign-compare
                        -w
                        )

target_compile_definitions(sla PRIVATE USING_ARCHIVE_LIB)