from cffi import FFI
import os


__all__ = ["compacta","descompacta"]

# Inicializar o FFI
ffi = FFI()

# Declarar a função C
ffi.cdef("""
    int compacta(const char* nomeArqBin, const char* nomeArqTxt);
int descompacta(const char* nomeArqBin, const char* nomeArqTxt);
""")

try:
    c_lib = ffi.dlopen(os.path.abspath("./codifica.dll"))
except OSError as e:
    print(f"Erro ao carregar biblioteca: {e}")

def compacta(nomeArqIn, nomeArqOut):
    return c_lib.compacta(ffi.new("char[]", nomeArqIn.encode('ascii')),ffi.new("char[]", nomeArqOut.encode('ascii')))

def descompacta(nomeArqIn, nomeArqOut):
    return c_lib.descompacta(ffi.new("char[]", nomeArqIn.encode('ascii')),ffi.new("char[]", nomeArqOut.encode('ascii')))
