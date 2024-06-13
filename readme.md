# AWS AccessKey Pair 조사

## 구현 목표

* HTTP 요청 응답으로 AccessKey Pair 생성 이후 N시간을 초과하는 IAM User의 User ID, Access Key ID을 반환

## 사용 기술

* Python 3.12.1
* boto3(Python용 AWS SDK(Boto3))