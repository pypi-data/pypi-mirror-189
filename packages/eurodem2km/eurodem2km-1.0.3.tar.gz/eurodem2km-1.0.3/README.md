Import the DemAPI class and use its method "getAltitude(lat: float, lon: float)" to get the location altitude'



DEVELOPMENT

Clone the code and install as an editable install using:
python -m pip install -e .

PACKAGING
Follow this fine tutorial:
https://realpython.com/pypi-publish-python-package/

Install in virtual environment the build and twine tools:
python -m pip install build twine keyrings.alt

Build:
python -m build

Check output:
twine check dist/*

Upload to PyPI:
twine upload dist/*