from setup import setup, find_packages

setup(
    name="graspi_netowrkx",
    version="0.1.0",
    author="qp",
    author_email="kazunesashi@gmail.com",
    description="graSPI implementation using the networkx python package",
    long_description=open('README.md').read(),  # Long description from your README file
    long_description_content_type="text/markdown",
    # url="https://github.com/username/my_project",  # Project URL (optional)
    packages=find_packages(),       # Automatically find packages in your project
    install_requires=[              # Dependencies, if any
        "requests",  # Example dependency
    ],
    classifiers=[                   # Metadata for searchability
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',        # Python version requirement
)