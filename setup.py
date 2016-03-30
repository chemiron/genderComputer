from setuptools import setup, find_packages

setup(name='genderComputer',
      version='0.0.2',
      description="Python tool that tries to infer a person's gender from their name (mostly first name) and location (country)",
      long_description=open('readme.md').read(),
      author='Alexander Serebrenik',
      author_email='a.serebrenik tue.nl',
      packages=find_packages(),
      install_requires=["nameparser", "unidecode"],
      classifiers=[
          'Development Status :: Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Operating System :: Unix',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Topic :: Utilities',
      ],
)
