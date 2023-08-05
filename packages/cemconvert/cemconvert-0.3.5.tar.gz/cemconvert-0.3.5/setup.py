from setuptools import setup, find_packages
setup(
    name="cemconvert",
    version="0.3.5",
    packages=find_packages(),
    scripts = ['bin/cemconvert','bin/get_camd_cems'],
    python_requires='>3.5',
    setup_requires=['numpy>=1.12','pandas>=0.20'],
    author_email='beidler.james@epa.gov'
)
