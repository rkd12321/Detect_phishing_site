# Detect_phishing_site
opensquat를 활용하여 특정 도메인과 유사한 사이트 탐지 및 알람 받기<br>
opensquat : 키워드와 유사한 도메인을 찾아주는 오픈소스<br> 
(ex: 키워드 'google' 검색시 g00gle, goog1e 등 키워드와 유사한 도메인들이 있는지 검색하여 저장함)

## 1. [opensquat 설치하기](https://github.com/atenreiro/opensquat#how-to-install)
### 1) 해당 URL 확인하여 opensquat 설치
```bash
sudo yum isntall python3 pip3 # python3 및 pip3 설치
git clone https://github.com/atenreiro/opensquat # opensquat 다운로드
pip3 install -r requirements.txt # opensquat 설치에 필요한 패키지 설치
```
---
### 2) /opensquat/output.py 수정
---
