LIBSLA=sleigh-2.1.0/src/libsla.a


OS = $(shell uname -s)
ifeq ($(OS),Darwin)
    WHOLE_FLAGS=-Wl,-all_load $(LIBSLA) -Wl,-noall_load
else
    WHOLE_FLAGS=-Wl,--whole-archive $(LIBSLA) -Wl,--no-whole-archive
endif

pypcode-native.so: $(LIBSLA) pypcode-native.cc pypcode-native.h
	g++ -shared -o $@ \
		$(WHOLE_FLAGS) \
		-fPIC pypcode-native.cc

$(LIBSLA):
	make -C sleigh-2.1.0/src CFLAGS="-fPIC" libsla.a
