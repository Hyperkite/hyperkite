from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
     name = 'hyperkite',  
     packages = ['hyperkite'],
     version = '0.1.5',
     description = "Hyperkite is a parameter optimization tool inspired by the way you train your machine learning models. From academia to industry, the tool is designed to optimize hyper-parameters and manage machine learning training experiments, using the most powerful algorithms in the most simple way.",
     author = "Hyperkite",
     author_email = "admin@hyperkite.ai",
     url = 'https://github.com/Hyperkite/hyperkite',
     download_url = 'https://github.com/Hyperkite/hyperkite/archive/v0.1.2.tar.gz',
     keywords = ['hyper-parameter', 'optimization', 'tool', 'bayesian'],
     license = 'MIT',
     install_requires = ['requests', 'vcrpy', 'nose'],
     classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
         ],
     zip_safe = False)
