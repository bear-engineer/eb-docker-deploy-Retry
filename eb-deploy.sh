#!/usr/bin/env bash
pipenv lock --requirements > requirements.txt

git add -f .secrets
git add requirements.txt
eb deploy --profile FC-8th-el --staged

git reset HEAD .secrets requirements.txt
rm -rf requirements.txt