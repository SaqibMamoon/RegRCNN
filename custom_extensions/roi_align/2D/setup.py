"""
Created at 07.11.19 19:12
@author: gregor

"""

import os, sys, site
from pathlib import Path

# recognise newly installed packages in path
site.main()

from setuptools import setup
from torch.utils import cpp_extension

dir_ = Path(os.path.dirname(sys.argv[0]))

setup(name='RoIAlign extension 2D',
      ext_modules=[cpp_extension.CUDAExtension('roi_al_extension', [str(dir_/'src/RoIAlign_interface.cpp'),
                                                                    str(dir_/'src/RoIAlign_cuda.cu')])],
      cmdclass={'build_ext': cpp_extension.BuildExtension}
      )
