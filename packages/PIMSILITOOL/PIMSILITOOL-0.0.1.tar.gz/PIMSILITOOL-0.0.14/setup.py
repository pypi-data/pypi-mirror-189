import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pimsilitool")
__version__ = '0.0.14'

with open("README.md", "r") as rf:
    long_description = rf.read()
# installrequires = ['azure', 'pywin32',  'reportlab', ]

setup(
      name='PIMSILITOOL',
      version =__version__,
      description = 'Provides tools for PIMS ILI analysis',
      long_description = long_description,      
      author = 'G2 Integrated Solutions.',
      author_email = 'support@g2-is.com',
      url = 'http://g2-is.com',
      license = 'license.txt',
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 3",
          "Operating System :: Microsoft :: Windows",
           ],
      project_urls={
          "Documentation": "https://knowledgecenter.g2-is.com/products/inlineinspection-tool/",
          "Code": "https://github.com/G2IntegratedSolutions/inlineinspection/",
          "Issue tracker": "https://github.com/G2IntegratedSolutions/inlineinspection/",
        },
      maintainer="G2 Integrated Solutions",
      maintainer_email="support@g2-is.com",
      packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests", "eol"]),
      python_requires='>=3.6',
      package_dir = {'pimsilitool':'pimsilitool'},
      package_data = {'pimsilitool': ['esri\\toolboxes\\*', 'packages\\*']},
      # data_files=[('liquidshca', ['liquidshca/*'])],
      #install_requires = installrequires,
      #install_requires = ['azure', 'pywin32',  'reportlab', ],
                          # 'evoleap_licensing',],
      )


