#!/usr/bin/env python
import os
import subprocess
import argparse

MODES = ['base', 'dev', 'production']

def mode_fuction(mode):
    if mode == 'base':
        build_base()
    elif mode == 'dev':
        build_dev()
    elif mode == 'production':
        build_production()
    else:
        raise ValueError(f'{MODES} 에 속하는 모드만 가능하다.')

def build_base():
    try:
        # pipenv lock로 requirements.txt 생
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)

        # docker build
        subprocess.call('docker build -t eb-docker-re:base -f Dockerfile.base .', shell=True)
    finally:
        # build 종료 후 requirements.txt 파일 삭제
        os.remove('requirements.txt')

def build_dev():
    try:
        # pipenv lock로 requirements.txt 생
        subprocess.call('pipenv lock --requirements --dev> requirements.txt', shell=True)

        # docker build
        subprocess.call('docker build -t eb-docker-re:dev -f Dockerfile.dev .', shell=True)
    finally:
        # build 종료 후 requirements.txt 파일 삭제
        os.remove('requirements.txt')

def build_production():
    try:
        # pipenv lock로 requirements.txt 생
        subprocess.call('pipenv lock --requirements > requirements.txt', shell=True)

        # docker build
        subprocess.call('docker build -t eb-docker-re:production -f Dockerfile.production .', shell=True)
        # root = '/var/log/django'
        # if root:
        #     return True
        # else:
        #     subprocess.call('mkdir /var/log/djnago', shell=True)
    finally:
        # build 종료 후 requirements.txt 파일 삭제
        os.remove('requirements.txt')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', help='Docker build mode [base, dev]')
    args = parser.parse_args()

    # 모듈 호출에 옵션으로 mode를 전달한 경우
    if args.mode:
        mode = args.mode.strip().lower()


    # 사용자가 입력한 mode를  선택한 경우
    else:
        while True:
            print('Select mode')
            for index, mode in enumerate(MODES, start=1):
                print(index, mode)
            selected_mode = input('Choice: ')
            try:
                mode_index = int(selected_mode) - 1
                mode = MODES[mode_index]
                break
            except IndexError:
                print('번호를 입력하시오')

    # 선택된 mode에 해당하는 함수를 실
    mode_fuction(mode)
