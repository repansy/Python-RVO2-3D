from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as _build_ext
from Cython.Build import cythonize


class Build3dRvo2Ext(_build_ext):
    """Builds 3D RVO2 before our module."""

    def run(self):
        # Build RVO2-3D
        import os
        import os.path
        import subprocess

        build_dir = os.path.abspath('build/RVO2-3D')
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)
            subprocess.check_call(['cmake', '../..', '-DCMAKE_CXX_FLAGS=-fPIC'],
                                  cwd=build_dir)
        subprocess.check_call(['cmake', '--build', '.'], cwd=build_dir)

        _build_ext.run(self)


extensions = [
    Extension('rvo2_3d', ['src/*.pyx'],
              include_dirs=['src'],
              libraries=['RVO'],
              library_dirs=['build/RVO2-3D/src'],
              extra_compile_args=['-fPIC']),
]

setup(
    name="pyrvo2",
    ext_modules=cythonize(extensions),
    cmdclass={'build_ext': Build3dRvo2Ext},
)