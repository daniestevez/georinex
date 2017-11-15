#!/usr/bin/env python
req = ['nose','numpy','numpy','xarray','netcdf4','pathlib2']
# %%
from setuptools import setup
setup(name='pyrinex',
      packages=['pyrinex'],
	  description='Python RINEX reader that is very fast',
	  author='Michael Hirsch, Ph.D.',
      version='1.0.0',
	  url='https://github.com/scivision/pyrinex',
	  install_requires=req,
      python_requires='>=2.7',
      extras_requires={'plot':['matplotlib','seaborn'],
                       'deprecated':['pandas'],},
	  )
