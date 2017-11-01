from setuptools import setup

setup(name='netoi_check',
      version='0.5',
      description='CLI for solution submission to NetOI',
      url='http://github.com/lionell/netoi-check',
      author='Ruslan Sakevych',
      author_email='xlionell@gmail.com',
      license='MIT',
      packages=['netoi_check'],
      entry_points={
          'console_scripts': [
              'netoi-check=netoi_check:main',
          ],
      },
      install_requires=['requests', 'lxml', 'tabulate'],
      #python_requires='>=3',
      zip_safe=False)
