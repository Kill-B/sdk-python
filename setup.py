from setuptools import setup, find_packages

setup(
    name="killb-sdk-python",
    version="1.0.1",
    packages=find_packages(),
    requires=['requests'],
    author="Kill-B",
    description="SDK for KillB API V2",
    long_description=open('./README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Kill-B/sdk-python",
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent']
)
