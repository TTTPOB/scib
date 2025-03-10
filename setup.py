import subprocess
import sys
import os

from setuptools import setup

# get compiler path
gxx = os.environ.get("CXX", "g++")

try:
    cmd = (
        f"{gxx} -std=c++11 -O3 scib/knn_graph/knn_graph.cpp -o scib/knn_graph/knn_graph.o"
    )
    sys.stdout.write("Compile knn_graph C++ code for LISI metric...\n")
    sys.stdout.flush()
    subprocess.check_output(
        cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True
    )
except subprocess.CalledProcessError as exc:
    sys.stdout.write(
        f"Failed to compile knn_graph for LISI - skipping...\n{exc.returncode}\n{exc.output}"
    )
    sys.stdout.flush()

setup()
