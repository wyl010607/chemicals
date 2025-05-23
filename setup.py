"""Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2016, 2017, 2018, 2019, 2020 Caleb Bell
<Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from setuptools import setup
from wheel.bdist_wheel import bdist_wheel
import os
import shutil
from pathlib import Path
import tempfile

    
class bdist_wheel_light(bdist_wheel):
    description = "Build a light wheel package without large data files"
    
    def run(self):
        pkg_dir = Path(os.path.abspath('chemicals'))
        
        # Files to exclude (relative to chemicals directory)
        exclude_files = [
            'Law',
            'Environment/Syrres logP data.csv.gz',
            'Identifiers/dippr_2014.csv',
            'Misc/ChemSep8.32.xml',
            'Identifiers/chemical identifiers pubchem large.tsv',
            'Identifiers/chemical identifiers pubchem small.tsv',
            'Identifiers/chemical identifiers example user db.tsv',
        ]
        
        # Create temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            moved_files = []
            
            try:
                # Move files to temporary location
                for rel_path in exclude_files:
                    orig_path = pkg_dir / rel_path
                    if orig_path.exists():
                        # Create path in temp dir maintaining structure
                        temp_path = Path(temp_dir) / rel_path
                        temp_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        if orig_path.is_dir():
                            shutil.move(str(orig_path), str(temp_path))
                        else:
                            shutil.move(str(orig_path), str(temp_path))
                        moved_files.append((orig_path, temp_path))
                
                # Build the wheel
                super().run()
                
            finally:
                # Restore moved files
                for orig_path, temp_path in moved_files:
                    if temp_path.exists():
                        orig_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(temp_path), str(orig_path))


classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Manufacturing',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: MacOS',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: BSD',
    'Operating System :: POSIX :: Linux',
    'Operating System :: Unix',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Education',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
    'Topic :: Scientific/Engineering :: Chemistry',
    'Topic :: Scientific/Engineering :: Physics',
]


setup(
  name = 'chemicals',
  packages = ['chemicals'],
  license='MIT',
  version = '1.3.3',
  description = 'Chemical properties component of Chemical Engineering Design Library (ChEDL)',
  author = 'Caleb Bell',
  install_requires=['fluids>=1.1.0', "scipy>=1.6.0", 'numpy', 'pandas'],
  extras_require = {
      'Coverage documentation':  ['wsgiref>=0.1.2', 'coverage>=4.0.3']
  },
  long_description=open('README.rst').read(),
  platforms=["Windows", "Linux", "Mac OS", "Unix"],
  author_email = 'Caleb.Andrew.Bell@gmail.com',
  url = 'https://github.com/CalebBell/chemicals',
  download_url = 'https://github.com/CalebBell/chemicals/tarball/1.3.3',
  keywords = ['chemical engineering', 'chemistry', 'mechanical engineering',
  'thermodynamics', 'databases', 'cheminformatics', 'engineering','viscosity',
  'density', 'heat capacity', 'thermal conductivity', 'surface tension',
  'combustion', 'environmental engineering', 'solubility', 'vapor pressure',
  'equation of state', 'molecule'],
  classifiers = classifiers,
  package_data={'chemicals': ['Critical Properties/*', 'Density/*',
  'Electrolytes/*', 'Environment/*', 'Heat Capacity/*', 'Identifiers/*',
  'Law/*', 'Misc/*', 'Phase Change/*', 'Reactions/*', 'Safety/*',
  'Solubility/*', 'Interface/*', 'Triple Properties/*',
  'Thermal Conductivity/*',
  'Vapor Pressure/*', 'Viscosity/*']},

    cmdclass={
        'bdist_wheel_light': bdist_wheel_light,
    }  
)
