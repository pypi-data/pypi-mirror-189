# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['akhdefo_functions']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'akhdefo-functions',
    'version': '2.2.38',
    'description': 'Land Deformation Monitoring Using Optical Satellite Imagery',
    'long_description': "\n# Akhdefo: \n# Background of Akh-Defo:\nAKh-Defo is combination of two different words 1) Akh in Kurdish language means land, earth or soil (origion of the word is from Kurdish badini dailect) 2) Defo is short of English word deformation.\n\n# Recommended Citation:\nMuhammad M, Williams-Jones G, Stead D, Tortini R, Falorni G and Donati D (2022) Applications of ImageBased Computer Vision for Remote Surveillance of Slope Instability.Front. Earth Sci. 10:909078. doi: 10.3389/feart.2022.909078\n\n# Updates:\n* Akhdefo version one is deprecated please use Akhdefo version 2.\n* Akhdefo now can run on the cloud for real-time processing\n* Akhdefo now consist of 12 Modules that performs end to end python-based GIS and Image Processing and Custumized Figure generation\n\n# Usage:\n* [download anaconda environment file](akhdefov2.yml) \n\nPlease visit the GITHUB homepage to download the file\n\n* [download python package requirement text](pip_req.txt) \n\nPlease visit the GITHUB homepage to download the file\n\n* Create new python Anaconda environment using the below command\n\n```python\nconda env create -f akhdefov2.yml\n\n```\n\n* Install required python packages using below command\n\n```python\npip install -r pip_req.txt\n```\n\n* Now install Akhdefo using the below command\n\n```python\npip install akhdefo-functions\n```\n\n# User Guide\n* Under construction will be released soon!\n\n# Akhdefo Functions Summary\n\n##  Preprocessing functions to unzip and sort images\n\n```python\nfrom akhdefo_functions import copyImage_Data, copyUDM2_Mask_Data , unzip\n```\n\n##   Import Module to mosaic and crop raster to Area of Interest using shapefile\n\n```python\nfrom akhdefo_functions import Mosaic, Crop_to_AOI\n```\n\n##  Import Module to filter rasters\n\n```python\nfrom akhdefo_functions import Filter_PreProcess\n```\n\n## Import Module to calculate triplet raster velocities\n\n```python\n from akhdefo_functions import DynamicChangeDetection\n \n ```\n\n##  Import Modules for plotting\n\n```python\nfrom akhdefo_functions import akhdefo_viewer\nfrom akhdefo_functions import plot_stackNetwork\nfrom akhdefo_functions import Akhdefo_resample\nfrom akhdefo_functions import Akhdefo_inversion\n```\n\n##  Import Module to process stacked triplet velocities and collect velocity candidate points\n\n```python\nfrom akhdefo_functions import stackprep'\n```\n##  Python module to coregister satallite images\n\n```python\nfrom akhdefo_functions  import  Coregistration\n```\n\n##  python module to process and calculate timestamp linear deformation rates\n\n```python\nfrom akhdefo_functions import  Time_Series\n```\n\n##  python module to plot timeseries profile for selected points\n\n```python\nfrom  akhdefo_functions import  akhdefo_ts_plot\n\n```",
    'author': 'Mahmud Mustafa Muhammad',
    'author_email': 'mahmud.muhamm1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/mahmudsfu/AkhDefo',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
