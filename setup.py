from setuptools import setup

setup(name='netoi_check',
      version='0.1',
      description='CLI for solution submission to NetOI',
      url='http://github.com/lionell/netoi-check',
      author='Ruslan Sakevych',
      author_email='xlionell@gmail.com',
      license='MIT',
      packages=['netoi_check'],
      scripts=['bin/netoi-check'],
      install_requires=['lxml', 'tabulate'],
      python_requires='>=3',
      zip_safe=False)
