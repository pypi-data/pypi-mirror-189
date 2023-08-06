from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dominant_image_color',
    version='1.0.0',
    description='Get the most frequent color from an image',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='MD Sameer',
    author_email='contact@mdsameer.com.np',
    packages=find_packages(),
    install_requires=['Pillow'],
)
