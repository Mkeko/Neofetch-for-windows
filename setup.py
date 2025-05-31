from setuptools import setup, find_packages

setup(
    name="easywinfetch",
    version="1.0.1",
    packages=find_packages(),
    package_data={
        "easywinfetch": ["config.yml"],
    },
    install_requires=[
        "wmi",
        "psutil",
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'easywinfetch=easywinfetch.neofetch_win:display_info',
        ],
    },
    author="Mkeko",
    description="A Windows system information display tool similar to Neofetch",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mkeko/Neofetch-for-windows",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)
