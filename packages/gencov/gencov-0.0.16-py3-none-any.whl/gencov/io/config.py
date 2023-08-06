import lzma
import os
import platform
import tarfile
import shutil
import subprocess


PACKAGE_PATH = os.path.dirname(__file__)
EXT_PATH = os.path.join(PACKAGE_PATH, "ext")
BIN_PATH = os.path.join(PACKAGE_PATH, "bin")

KERNEL = platform.system().lower()
ARCHITECTURE = platform.machine().lower().replace("amd64", "x86_64")
SYSTEM = f"{KERNEL}.{ARCHITECTURE}"


def set_executable(path):
    if KERNEL != "windows":
        os.chmod(path, os.stat(path).st_mode | 0o111)


def get_bin_path(*path):
    path = os.path.join(BIN_PATH, *path)
    if os.path.isfile(path):
        return path
    if os.path.isfile(f"{path}.exe"):
        return f"{path}.exe"
    return None


def decompress_tar_archive(in_path, in_base_path, out_path):
    tmp_dir = f"{out_path}.tmp"
    try:
        os.mkdir(tmp_dir)
        with tarfile.open(in_path, "r") as in_file:
            in_file.extractall(tmp_dir)
            shutil.move(os.path.join(tmp_dir, in_base_path), out_path)
    finally:
        if os.path.isdir(tmp_dir):
            shutil.rmtree(tmp_dir)


def decompress_lzma_file(in_path, out_path, chunk_size=65536):
    with lzma.open(in_path, "rb") as in_file:
        with open(out_path, "wb") as out_file:
            chunk = in_file.read(chunk_size)
            while chunk:
                out_file.write(chunk)
                chunk = in_file.read(chunk_size)


def make_bin():
    if os.path.isdir(BIN_PATH):
        shutil.rmtree(BIN_PATH)
    os.mkdir(BIN_PATH)
    compatible_systems = [SYSTEM]
    if SYSTEM == "darwin.arm64":
        compatible_systems.append("darwin.x86_64")
    installed = {}
    for lib in ["libbigwig", "samtools", "ucsc"]:
        for compatible_system in compatible_systems:
            path = os.path.join(EXT_PATH, lib, f"{compatible_system}.tar.xz")
            if os.path.isfile(path):
                out_path = os.path.join(BIN_PATH, lib)
                decompress_tar_archive(path, compatible_system, out_path)
                installed[lib] = out_path
                break
    if "libbigwig" in installed:
        shutil.rmtree(os.path.join(installed["libbigwig"], "docs"))
        shutil.rmtree(os.path.join(installed["libbigwig"], "test"))
        for name in os.listdir(installed["libbigwig"]):
            set_executable(os.path.join(installed["libbigwig"], name))
    if "samtools" in installed:
        for name in os.listdir(os.path.join(installed["samtools"], "bin")):
            set_executable(os.path.join(installed["samtools"], "bin", name))
    if "ucsc" in installed:
        for name in os.listdir(installed["ucsc"]):
            set_executable(os.path.join(installed["ucsc"], name))
    if KERNEL in ["linux", "darwin"] and "libbigwig" in installed:
        for lib in ["bigwig_reader", "bigbed_reader", "bbi_header_reader"]:
            path = os.path.join(PACKAGE_PATH, "signal_c_lib", f"{lib}.c")
            out_path = os.path.join(BIN_PATH, lib)
            cmd = [
                "gcc", path, os.path.join(installed["libbigwig"], "libBigWig.a"),
                "-I", installed["libbigwig"], "-lm", "-lz", "-lcurl", "-O3",
                "-o", out_path]
            process = subprocess.run(cmd, capture_output=True)
            if process.returncode:
                message = process.stderr.strip().decode()
                raise RuntimeError(f"failed to compile {lib}: {message}")
            set_executable(out_path)
    if KERNEL == "windows" and "libbigwig" in installed:
        for lib in ["bigwig_reader.exe", "bigbed_reader.exe", "bbi_header_reader.exe"]:
            shutil.copyfile(
                os.path.join(installed["libbigwig"], "bin", lib),
                os.path.join(BIN_PATH, lib))
    decompress_lzma_file(
        os.path.join(EXT_PATH, "pyfaidx.py.xz"),
        os.path.join(BIN_PATH, "pyfaidx.py"))


if not os.path.isdir(BIN_PATH):
    make_bin()


BIGWIG_READER_BIN = get_bin_path("bigwig_reader")
BIGWIG_INFO_BIN = get_bin_path("ucsc", "bigWigInfo")
BIGWIG_TO_BEDGRAPH_BIN = get_bin_path("ucsc", "bigWigToBedGraph")
BEDGRAPH_TO_BIGWIG_BIN = get_bin_path("ucsc", "bedGraphToBigWig")
BIGBED_READER_BIN = get_bin_path("bigbed_reader")
BIGBED_INFO_BIN = get_bin_path("ucsc", "bigBedInfo")
BBI_HEADER_READER = get_bin_path("bbi_header_reader")
SAMTOOLS_BIN = get_bin_path("samtools", "bin", "samtools")

PYFAIDX_MOD = get_bin_path("pyfaidx.py")

FORCE_STD_LIB = False

CACHE = None
BIN_SIZE = 10
DEFAULT_VALUE = 0
FILL_ENTRIES = False
