#!/usr/bin/env python
import os
import subprocess

try:
    subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)
    subprocess.call('git add -f .secrets', shell=True)
    subprocess.call('git add requirements.txt', shell=True)
    subprocess.call('eb deploy --profile FC-8th-el --staged', shell=True)
    # pipenv lock로 requirements.txt 생

finally:
    # build 종료 후 requirements.txt 파일 삭제
    subprocess.call('git reset HEAD .secrets requirements.txt', shell=True)
    os.remove('requirements.txt')

