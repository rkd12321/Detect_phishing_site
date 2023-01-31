#-*- coding:utf-8 -*-
import os
import re
import urllib.request
import logging, requests, json, random
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.webhook import WebhookClient

slack_web_hook_url = "[Input Slack Web Hook URL]"
webhook = WebhookClient(slack_web_hook_url)

# logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

## slack 함수 ##

# 웹 훅 사용하기
def webhook_send(title, filename):
    response = webhook.send(
        text="fallback",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": title
                }
            },
            {
                "type": "image",
                "title": {
                    "type": "plain_text",
                    "text": "Screen_Shot_"+filename,
                    },
                "image_url": "https://urlscan.io/liveshot/?width=1600&height=1200&url=http://"+filename,
                "alt_text": filename
            }
        ]
    )

## 피싱탐지 시작 웹훅 메세지
def webhook_send_msg(start_message):
    response = webhook.send(
        text="fallback",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": start_message
                }
            }
        ]
    )
## slack 함수 끝 ##

## 파일 문자열 중복 검증 함수 ##

def check_string():
  ## url 비교를 위한 저장 경로 ##
  save_files_name = open("/home/ec2-user/results.txt") # opensquat 원본 결과값을 누적으로 관리하기 위한 파일 및 경로
  with save_files_name as temp_f:
    datafile = temp_f.readlines()
  for line in datafile:
    if split_strings in line:
      return True # The string is found
  return False # The string does not exist in the file
## 파일 문자열 중복 검증 함수 끝 ##

## 내용 없는 파일 확인 함수 ##
def check_null():
    check_null_file = "/home/ec2-user/opensquat/results.txt" # opensquat 원본 결과값 경로
    file_size = os.stat(check_null_file).st_size
    if file_size == 0:
        return True # 파일 용량이 0이면 참
    else:
        return False # 파일 용량이 0이 아니면 거
## 내용 없는 파일 확인 함수 끝 ##

## 오픈소스 실행 결과값 경로 ##
urlfiles = open("/home/ec2-user/phishing/opensquat/results.txt", "r")

urls = urlfiles.readlines()
## url 비교를 위한 저장 경로 ##
save_files = open("/home/ec2-user/results.txt", "a")
save_files_read = open("/home/ec2-user/results.txt", "r")

## 피싱 도메인 검색 시작 ##
start_send="`Start phishing detection`"
webhook_send_msg(start_send)
for url in urls:
    url_name = str(url)
    strings = url_name[7:]
    split_strings = strings.strip('\n')
    if check_string():
        print('기탐지 URL')
    elif check_null():
        print('탐지URL 없음')
        print(file_size)
    else:
        print('신규 URL')
        save_files.write(split_strings+'\n')
        print('피싱 url : '+strings)
        file_names = split_strings + ".png"
        print('파일명 : '+file_names)
        send_text = '*피싱의심 사이트 탐지*'+'\n'+'*탐지 URL : *'+'`hxxp://'+split_strings+"`"+"<@[slack user id]>" # slack 멘션(@abc)할때 나오는 id
        send_image = '/home/ec2-user/phishing/screenshot/'+file_names # 라이브 스크린샷의 경우, 볼때 변하기 때문에 검색 시 확인한 스크린샷을 따로 저장
        url_scan = "https://urlscan.io/liveshot/?width=1600&height=1200&url=http://"+split_strings
        urllib.request.urlretrieve(url_scan, send_image)
        
## slack send
        webhook_send(send_text, split_strings)
