import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codefast",
    version="0.9.23",  # Latest version .
    author="slipper",
    author_email="r2fscg@gmail.com",
    description="A package for faster coding.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/private_repo/codefast",
    packages=setuptools.find_packages(),
    install_requires=[
        'colorlog', 'lxml', 'requests', 'tqdm',
        'smart-open', 'bs4', 'arrow', 'termcolor',
        'pydub', 'pycryptodome', 'requests-toolbelt'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
