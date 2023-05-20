from setuptools import find_packages,setup



setup(
    name="ML Project",
    version='0.0.1',
    author='Anirudh-Aravind',
    author_email='anirudhparavind@gmail.com',
    packages=find_packages(),
    install_requires = ['pandas','numpy','seaborn']    
)