from setuptools import setup, find_packages

setup(
    name='buscophylo',
    version='1.2.1',
    author='Alae-eddine Sahbou',
    author_email='alae.shb147@gmail.com',
    description='BuscoPhylo is a free, online pipeline for performing BUSCO-based phylogenomic analysis. It quickly analyzes genome sequences in FASTA format and provides results ready for publication. The user-friendly interface makes it accessible for anyone to use.',
    long_description='''BuscoPhylo is a free online pipeline for phylogenomic analysis using BUSCO. It quickly analyzes FASTA formatted genome sequences and provides ready-to-publish results. The user-friendly interface makes it easy to use for anyone.

To access the BuscoPhylo API, you need to log in to the user dashboard and have an API token for authentication. Your API token can be found under your user name in the dashboard. To install the BuscoPhylo API, simply run "pip install buscophylo" in your terminal.

To use the BuscoPhylo API, import the buscophylo module, initiate an instance of the BuscoPhylo class, and set your API token, project name, lineage, mode, and directory. Finally, run the run function. Example code:

from buscophylo import BuscoPhylo

buscophylo = BuscoPhylo()

buscophylo.Token("YOUR_TOKEN")

buscophylo.Project_Name("Project_Name")

buscophylo.lineage("Lineage")

buscophylo.mode("Mode")

buscophylo.directory("Directory")

buscophylo.run()

If you use the BuscoPhylo API in your work, please cite it in your publication to acknowledge its contribution. BuscoPhylo is also available on PyPI at https://pypi.org/project/BuscoPhylo/.''',
    url='https://buscophylo.inra.org.ma/',
    packages=find_packages(),
    py_modules=['buscophylo'],
    install_requires=[
        'requests',
    ]
)
