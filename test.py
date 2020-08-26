
import json
import urllib.request
import re
from urllib.parse import quote
# Create your views here.
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext
# Create your views here.
def text():
    TMD_KEY = '37a3092ff9c0a61c3819bc65e4ab09c5'

    LIST_URL = f"https://api.themoviedb.org/3/movie/66115?api_key={TMD_KEY}&language=ko-KR"

    request = urllib.request.Request(LIST_URL)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        d = json.loads(response_body.decode('utf-8'))
        if (d):
            return d
        else:
            return None

    else:
        print("Error Code:" + rescode)

def moviePickUp():
    # the movie db key
    TMD_KEY = '37a3092ff9c0a61c3819bc65e4ab09c5'
    # 영화 리스트를 여러 페이지 가져오기
    for n in range(1, 6):
        num = str(n)
        # 영화 목록 url
        LIST_URL = f"https://api.themoviedb.org/3/discover/movie?api_key={TMD_KEY}&language=ko-KR&page={num}"
        request = urllib.request.Request(LIST_URL)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            resDatas = json.loads(response_body.decode('utf-8'))

        for resData in resDatas['results']:
            # 영화의 TMD id

            tmd_id = resData['id']

            # 영화 detail url
            DETAIL_URL = f"https://api.themoviedb.org/3/movie/{tmd_id}?api_key={TMD_KEY}&language=ko-KR"
            request = urllib.request.Request(DETAIL_URL)
            response = urllib.request.urlopen(request)
            if (rescode == 200):
                response_body = response.read()
                detailData = json.loads(response_body.decode('utf-8'))
            # 영화 감독 //
            CREDITS_URL = f"https://api.themoviedb.org/3/movie/{tmd_id}/credits?api_key={TMD_KEY}"
            request = urllib.request.Request(CREDITS_URL)
            response = urllib.request.urlopen(request)
            if (rescode == 200):
                response_body = response.read()
                resdirectors = json.loads(response_body.decode('utf-8'))

            for resdirector in resdirectors['cast']:
                # job이 Director인 사람의 이름 찾기
                if 'job' in resdirector :
                    if (resdirector['job'] == 'Director'):
                        director = resdirector['name']
                        break
                    else:
                        director = ""
            # // 영화 감독

            # 영화 회사정보
            resDetailData = detailData['production_companies']
            if resDetailData:
                company = resDetailData[0]['name']
            else:
                # 영화 회사 정보가 없는 경우
                company = ""

            # 홈페이지가 있는경우와 없는 경우 구분
            # print(detailData.json().get('homepage'))
            if detailData['homepage'] != None:
                homepage = detailData['homepage']
                # print(homepage)
            else:
                homepage = ""

            # 장르가 있는지 없는지
            if detailData['genres']:
                genre = detailData['genres'][0]['name']
            else:
                genre = ""
            print(genre)
            print(resData['title'])


moviePickUp()
