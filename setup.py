from setuptools import setup,find_packages
from pathlib import Path

setup(
    name="tgtoolkit",
    description="Toolkit to do repetitive tasks on Telegram.",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    version="0.1",
    author="Florian Wagner",
    author_email="florian@wagner-flo.net",
    url="https://github.com/wagnerflo/tgtoolkit",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: No Input/Output (Daemon)",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Communications :: Chat",
    ],
    license_files=["LICENSE"],
    python_requires=">= 3.12",
    install_requires=[
        "click >= 8.0.0",
        "Pyrogram >= 2.0.106"
        "TgCrypto >= 1.2.5",
    ],
    packages=find_packages(),
    entry_points = {
        "console_scripts": [
            "tgtkd=tgtoolkit.tkd:main",
        ],
    },
)
