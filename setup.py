from distutils.core import setup

setup(name='hybrid_ai_py',
      version='0.27',
      packages=['hybrid_ai_py'],
      license='Apache 2',
      py_modules=['hybrid_ai_py'],
      install_requires=
      [
        'sparqlwrapper', 'rdflib', 'openai',
      ],      

      long_description=open('README.md').read())
