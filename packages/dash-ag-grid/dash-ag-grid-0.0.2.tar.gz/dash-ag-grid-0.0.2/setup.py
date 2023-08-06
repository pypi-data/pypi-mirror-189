from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name="dash-ag-grid",
    version="0.0.2",
    author="Alex Johnson",
    author_email="alex@plotly.com",
    url="https://plotly.com/dash/",
    packages=["dash_ag_grid"],
    license="MIT",
    description="A Public stub for dash-ag-grid by Plotly",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Dash",
    ],
)
