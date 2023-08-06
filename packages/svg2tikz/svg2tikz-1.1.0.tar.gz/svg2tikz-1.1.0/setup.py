# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['svg2tikz',
 'svg2tikz.extensions',
 'svg2tikz.inkex',
 'svg2tikz.inkex.elements',
 'svg2tikz.inkex.tester']

package_data = \
{'': ['*']}

install_requires = \
['inkex>=1.2.2+dairiki.1,<2.0.0', 'lxml>=4.9.2,<5.0.0']

setup_kwargs = {
    'name': 'svg2tikz',
    'version': '1.1.0',
    'description': 'Tools for converting SVG graphics to TikZ/PGF code',
    'long_description': '# SVG2TikZ (Inkscape 1.x.x compatible)\n[![Documentation Status](https://readthedocs.org/projects/svg2tikz/badge/?version=latest)](https://svg2tikz.readthedocs.io/en/latest/?badge=latest)\n\nSVG2TikZ, formally known as Inkscape2TikZ ,are a set of tools for converting SVG graphics to TikZ/PGF code.\nThis project is licensed under the GNU GPL  (see  the [LICENSE](/LICENSE) file).\n\n## Documentation and installation\nAll the informations to install and use `SVG2TikZ` can be found in our [Documentation](https://svg2tikz.readthedocs.io/en/latest).\n\n## Changes, Bug fixes and Known Problems from the original\n\n- Now images can also be exported to tikz\n- Added a variable `/def /globalscale` to the output tikz document (standalone and tikz figure)\n- `/globalscale` when changed will scale the tikzfigure by transforming the vector coordinates.\n- `/globalscale` when changed will scale the tikzfigure by scaling the embedded images\n- The path element was not exported in correct coordinates. This is fixed\n- Added an entry to specify the path to be removed from absolute paths in the images. This is useful to work in a latex project directly\n\nKnown Problems\n- Currently only images that are "linked" in svg are exported. Base64 embed is not yet supported so avoid choosing embed option\n- Grouped elements will not work. So ungroup everything\n\nMore documentation can be found in the [docs/](/docs/index.rst) directory.\n',
    'author': 'ldevillez',
    'author_email': 'louis.devillez@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
