
"""
import setuptools

setuptools.setup(
    name="math", 
    version="4.0.0",
    author="author",
    packages=['math'],
    python_requires='>=3.3',
)
"""


def configuration(parent_package='',top_path=None):

    from numpy.distutils.misc_util import Configuration
    config = Configuration('packageapple',parent_package,top_path)
    config.add_subpackage('math')
    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())