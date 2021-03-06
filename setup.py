from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name='gogpy',
      packages=['gogpy'],
      description='use gog visualization system from Python',
      long_description=long_description,
      license='MIT',
      author='Aaron Schumacher',
      author_email='ajschumacher@gmail.com',
      url='https://github.com/ajschumacher/gogpy',
      download_url='https://github.com/ajschumacher/gogpy/tarball/0.0.2',
      version='0.0.2',
      install_requires=['requests'])
