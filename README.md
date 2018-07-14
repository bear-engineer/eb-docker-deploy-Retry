# Mission

- Dockerfile.dev 사용시와 Dockerfile.production 사용시 RDS내의 각각 다른 DB, 다른 S3버킷을 사용하도록 설정
- deploy.sh 스크립트 작성, 실행 시 .secrets 와 requirements 파일을 git 에 추가 후 eb deploy 에 배포
- 종료 후 git reset으로 .secrets 를 스테이징 영역에서 제거, requirements.txt 파일을 삭제