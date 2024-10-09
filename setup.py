from setuptools import setup, find_packages

setup(
    name='graspi_networkx',
    version='0.1.6',
    packages=find_packages(),
    install_requires=[
        'contourpy==1.3.0',
        'cycler==0.12.1',
        'fonttools==4.54.1',
        'kiwisolver==1.4.7',
        'matplotlib==3.9.2',
        'networkx>=3.2,<3.4',
        'numpy>=2.0.0,<2.1',
        'packaging==24.1',
        'pandas==2.2.3',
        'pillow==10.4.0',
        'pyparsing==3.1.4',
        'PyQt6==6.7.1',
        'PyQt6-Qt6==6.7.3',
        'PyQt6_sip==13.8.0',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.2',
        'scipy>=1.9.0,<1.14',
        'six==1.16.0',
        'tzdata==2024.2'
    ],
    python_requires='>=3.6,<3.10',
    author="Qi Pan",
    author_email="mleung8@buffalo.edu",
    description="A package that utilizes NetworkX functionality for GraSPI",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/gobrin111/graspi_networkx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"
    ],
)
