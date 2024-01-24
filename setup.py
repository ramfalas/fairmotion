# Copyright (c) Facebook, Inc. and its affiliates.

from setuptools import find_packages, setup

setup(
    name="fairmotion",
    version="0.0.4",
    description="fairmotion is FAIR's library for human motion research",
    url="https://github.com/facebookresearch/fairmotion",
    author="FAIR Pittsburgh",
    author_email="dgopinath@fb.com",
    install_requires=[
        "black",
        "matplotlib",
        "numpy",
        "pillow",
        "scikit-learn",
        "scipy",
        "tqdm",
    ],
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
