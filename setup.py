from setuptools import setup, find_packages

setup(
    name="pymgridbhu",
    package_dir={"": "src"},
    packages=find_packages("src"),
    version="0.0.0",
    python_requires=">=3.0",
    include_package_data=True,
    install_requires=[
        "requests",
        "pandas",
        "numpy",
        "cvxpy",
        "statsmodels",
        "matplotlib",
        "plotly",
        "cufflinks",
        "gym",
    ],
)
