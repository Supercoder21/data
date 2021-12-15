import setuptools

setuptools.setup(
    author="Shay Palachy",
    author_email="shay.palachy@gmail.com",
    name='chocobo',
    license="MIT",
    description='Functions like standerd deviation that help in statistics',
    version='v0.0.3',
    long_description='This package has functions that can be used for sorting data and statistics',
    url='https://github.com/Supercoder21/data',
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Data',
        'Topic :: Software Development :: Data :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
