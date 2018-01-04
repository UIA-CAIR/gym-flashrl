import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="gym-flashrl",
    version="1.0.0",
    author="Per-Arne Andersen",
    author_email="per@sysx.no",
    description="gym bindings for FlashRL",
    license="MIT",
    keywords="reinforcement-learning deep-learning machine-learning pygame game-environment",
    url="https://github.com/UIA-CAIR/gym-flashrl",
    install_requires=[
        'FlashRL'
    ],

    packages=[
        'gym_flashrl',
        'gym_flashrl.envs',
    ],
    package_data={'': []},
    long_description=read('README.MD'),
    classifiers=[],
)
