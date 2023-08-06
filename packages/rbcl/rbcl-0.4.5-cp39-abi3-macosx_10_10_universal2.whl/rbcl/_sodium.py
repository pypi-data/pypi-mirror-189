"""
Load sodium shared object file from this directory (with filepaths constructed for GH Actions),
and write it to disk in a temporary file location. The sodium binary can then be read from disk
directly and exported when the library is invoked without depending on linkage by the host OS.
"""
import platform
import tempfile
import importlib.util

# Determine OS type
pl = platform.system()

# Read sodium shared object file from disk
sodium_so = open(  # pylint: disable=consider-using-with
    "src/rbcl/sodium.pyd" if pl == "Windows" else "src/rbcl/sodium.so", "rb"
)
bs = sodium_so.read()
sodium_so.close()

# Generate a temporary file on disk and write sodium binary to it
LIB_EXT = ".pyd" if pl == "Windows" else ".so"
lib_path = tempfile.NamedTemporaryFile(suffix=LIB_EXT, delete=False).name  # pylint: disable=consider-using-with
sodium_tmp = open(lib_path, "wb")  # pylint: disable=consider-using-with
sodium_tmp.write(bs)
# Close temp file to avoid multiprocess access error on Windows
sodium_tmp.close()

# Load sodium binary from disk to be used by rbcl.py
_sodium = importlib.util.module_from_spec(
    importlib.util.spec_from_file_location("_sodium", lib_path)
)
