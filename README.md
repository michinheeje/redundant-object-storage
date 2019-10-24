# redundant-object-storage

## 준비물
ATOM IDE, AWS, Flask, NAVER CLOUD PLATFORM, Python

## 사용법
1. AWS와 NCP를 액세스 키를 발급 받아 액세스 키 ID와 보안 액세스 키를 꼭 기입하여 저장하세요.

2. https://console.aws.amazon.com/ec2/에서 Amazon EC2 콘솔을 열어 로그인합니다.</br>

3. Amazon Machine Image(AMI) 선택 페이지에 인스턴스에 대한 템플릿 역할을 하는 Amazon Machine Image(AMI)라는 기본 구성 목록이 표시됩니다. Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type을 선택합니다.

4. 인스턴스 유형 선택 페이지에서 인스턴스의 하드웨어 구성을 선택할 수 있습니다. t2.micro 유형을 선택합니다.</br>

5. 인스턴스 세부 정보 구성 디폴트 설정으로 다음: 스토리지 추가를 클릭하세요.</br>

6. 스토리지 추가에서는 기본 구성으로 다음: 태그 추가를 클릭합시오.</br>

7. 태그 추가도 디폴트 설정으로 다음: 보안 그룹 구성을 클릭하십시오.</br>

8. 유형을 사용 지정 TCP 선택하여 범트 범위 8000과 소스 0.0.0.0/0로 설정하여 검토 및 시작를 클릭하십시오.</br>

9. 검토에서는 시작하기를 클릭하십시오.</br>

10. 기존 키 페어 선택 또는 새 키 페어 생성에서는 생성을 하거나 기존에 있던 키를 선택하여 pem를 사용하십시오.</br>

11. SSH를 username은 ec2-user입니다.</br>

12. 다음과 같이 명령어를 입력하십시오.

`sudo su - `
`yum update -y`</br>
`reboot`</br>
`sudo su -`</br>
`aws configure`</br>
`aws configure --profile ncp`</br>
`pip install flask`</br>
`mkdir /uploads`</br>
`cd`</br>
`vi index.py`</br>
`crontab -e`</br>
`30 * * * * aws s3 sync /uploads/ s3://hwangheeje/`</br>
`30 * * * * aws --endpoint-url=https://kr.object.ncloudstorage.com s3 sync /uploads/ s3://hwangheeje/ --profile ncp`</br>
`* * * * * find /uploads -ctime +1 -exec rm -f {} \;`</br>
