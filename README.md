# Mission

- Dockerfile.dev 사용시와 Dockerfile.production 사용시 RDS내의 각각 다른 DB, 다른 S3버킷을 사용하도록 설정
- deploy.sh 스크립트 작성, 실행 시 .secrets 와 requirements 파일을 git 에 추가 후 eb deploy 에 배포
- 종료 후 git reset으로 .secrets 를 스테이징 영역에서 제거, requirements.txt 파일을 삭제


## Secret file

`Project Root/.secrets`

### Secret key
```
{
  "SECRET_KEY": "<Django secret key>"
}
```

### DB info
```
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "<host>",
      "PORT": 5432,
      "USER": "<user>",
      "PASSWORD": "<password>",
      "NAME": "<db name>"
    }
  }
}
```

### AWS S3
```
{
  "AWS_ACCESS_KEY_ID":"<ACCESS Key>",
  "AWS_SECRET_ACCESS_KEY":"<SECRET Key>",
  "AWS_STORAGE_BUCKET_NAME_DEV":"<DEV BUCKET NAME>",
  "AWS_STORAGE_BUCKET_NAME":"<PRODUCTION BUCKET NAME>",
  "AWS_DEFAULT_ACL":"private",
  "AWS_S3_REGION_NAME":"ap-northeast-2",
  "AWS_S3_SIGNATURE_VERSION":"s3v4"
}

```

## AWS S3 권한 < CORS 규칙 추가

### AWS CORS 규칙 위반

- CSS 내부에서 import 되는 웹폰트 등 외부에서 가져오는 링크가 거부됨으로 규칙을 추가해주어야 한다.

```
<!-- Sample policy -->
<CORSConfiguration>
	<CORSRule>
		<AllowedOrigin>*</AllowedOrigin>
		<AllowedMethod>GET</AllowedMethod>
		<MaxAgeSeconds>3000</MaxAgeSeconds>
		<AllowedHeader>Authorization</AllowedHeader>
	</CORSRule>

	# 추가된 부분
	<CORSRule>
	    # 요청을 보내온 도메인/주소를 무조건 허용
		<AllowedOrigin>http://localhost:8000</AllowedOrigin>
		<AllowedMethod>GET</AllowedMethod>
		<MaxAgeSeconds>3000</MaxAgeSeconds>
	</CORSRule>
</CORSConfiguration>

```