from setuptools import setup, find_packages


setup(name='clean_folder',
      version='1.0',
      description='A script for sorting files in a folder',
      url='http://github.com/dummy_user/useful',
      author='Stas Stryzhakov',
      author_email='kriegehund@gmail.com',
      license='Go_IT',
      packages=find_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.sort:main']})