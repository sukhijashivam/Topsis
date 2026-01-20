from setuptools import setup
from pathlib import Path

# Read README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="topsis-shivam-102303041",
    version="1.0.3",  # 🔴 VERSION MUST BE NEW
    author="Shivam Sukhija",
    author_email="shivamsukhija@example.com",
    description="A Python implementation of TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["topsis"],
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main"
        ]
    },
    python_requires=">=3.7",
)
