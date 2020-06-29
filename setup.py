import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sphinx-astrorefs",
    version="0.1.dev0",
    author="Jo Bovy",
    author_email="bovy@astro.utoronto.ca",
    description="Astro-style references in Sphinx documents",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    packages=["sphinx_astrorefs"],
    install_requires=["pybtex","latexcodec"]
)