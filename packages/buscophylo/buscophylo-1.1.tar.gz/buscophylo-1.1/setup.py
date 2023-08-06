from setuptools import setup, find_packages

setup(
    name='buscophylo',
    version='1.1',
    author='Alae-eddine Sahbou',
    author_email='alae.shb147@gmail.com',
    description='BuscoPhylo is a free, online pipeline for performing BUSCO-based phylogenomic analysis. It quickly analyzes genome sequences in FASTA format and provides results ready for publication. The user-friendly interface makes it accessible for anyone to use.',
    long_description="""This is a new code that creates a Python module "buscophylo" for tree-based phylogenetics. It has functions to set and retrieve token, project name, lineage, mode, project group, and directory information. The run function checks if all required information is set and raises a "ValueError" if any information is missing. It then validates the token by making a post request to the "https://buscophylo.inra.org.ma/api/post.php" API endpoint with the token as data. If the response is equal to "valid", the token is valid and a message is printed to the console indicating this. If the response is not equal to "valid", a "ValueError" is raised indicating that the token is not valid. The code also sets up color formatting for console messages on Windows and non-Windows systems. To use the module, import it and set all required information with the respective functions before calling buscophylo.run().""",
    url='https://buscophylo.inra.org.ma/',
    packages=find_packages(),
    py_modules=['buscophylo'],
    install_requires=[
        'requests',
    ]
)
