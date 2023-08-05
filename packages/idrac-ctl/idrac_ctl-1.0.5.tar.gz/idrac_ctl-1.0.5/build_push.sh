#!/bin/bash
# dev only
#twine_username="spyroot"
#twine_password="py@$V6n9$IjCUCZ*"

rm dist/*
python setup.py sdist
python setup.py bdist_wheel sdist
twine upload dist/*


