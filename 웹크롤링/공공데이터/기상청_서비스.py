import requests
from datetime import datetime, timedelta

# 기상청 초단기실황 조회 (실시간 날씨)

# 현재 시간 기준 base_date, base_time 계산
# 매시 40분 이후 발표되므로, 40분 이전이면 이전 시간 사용
now = datetime.now()
if now.minute < 40:
    now = now - timedelta(hours=1)

base_date = now.strftime('%Y%m%d')
base_time = now.strftime('%H00')

url = 'https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
params = {
    # 공공데이터포털에서 발급받은 인증키 (Decoding 키)
    'serviceKey': 'Kfh07Rkb5WAsh0TZ1baGNkuP6C3l78vhmJEz7uV9sZiUPOfVZ0sNo84Ay2m0kK1NTBrR4PC8IccsXZg+1v5OhQ==',
    'pageNo': '1',
    'numOfRows': '1000',
    'dataType': 'JSON',
    'base_date': base_date,
    'base_time': base_time,
    'nx': '60',       # 서울 종로구
    'ny': '127'
}

# API 요청
response = requests.get(url, params=params)

# 카테고리 한글 매핑
category_name = {
    'T1H': '기온(°C)',
    'RN1': '1시간 강수량(mm)',
    'REH': '습도(%)',
}

# 강수형태 코드
pty_code = {
    '0': '없음', '1': '비', '2': '비/눈', '3': '눈',
    '5': '빗방울', '6': '빗방울눈날림', '7': '눈날림'
}

if response.status_code == 200:
    data = response.json()
    result = data.get('response', {})
    header = result.get('header', {})

    if header.get('resultCode') == '00':
        items = result['body']['items']['item']
        print(f'=== 실시간 날씨 정보 (서울 종로구) ===')
        print(f'기준 시각: {base_date} {base_time}')
        print('-' * 35)
        for item in items:
            cat = item['category']
            if cat not in ('T1H', 'RN1', 'REH'):
                continue
            val = item['obsrValue']
            name = category_name.get(cat, cat)
            print(f'{name}: {val}')
    else:
        print(f"API 오류: {header.get('resultCode')} - {header.get('resultMsg')}")
else:
    print(f'요청 실패: {response.status_code}')

