import os
import json
import datetime as dt
import urllib.parse
import urllib.request
import urllib.error

# 기상청 단기예보 API
ENDPOINT = "https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"

# 서울(종로구 인근) 격자
NX = 60
NY = 127

# 단기예보 발표 시각
BASE_TIMES = ["0200", "0500", "0800", "1100", "1400", "1700", "2000", "2300"]


def get_base_datetime(now=None):
    if now is None:
        now = dt.datetime.now()

    hhmm = now.strftime("%H%M")
    candidates = [t for t in BASE_TIMES if t <= hhmm]

    if candidates:
        return now.strftime("%Y%m%d"), candidates[-1]

    # 02:00 이전이면 전날 23:00 사용
    prev = now - dt.timedelta(days=1)
    return prev.strftime("%Y%m%d"), "2300"


def request_weather(service_key, nx=NX, ny=NY):
    base_date, base_time = get_base_datetime()
    params = {
        "serviceKey": "Kfh07Rkb5WAsh0TZ1baGNkuP6C3l78vhmJEz7uV9sZiUPOfVZ0sNo84Ay2m0kK1NTBrR4PC8IccsXZg%2B1v5OhQ%3D%3D",
        "pageNo": "1",
        "numOfRows": "1000",
        "dataType": "JSON",
        "base_date": base_date,
        "base_time": base_time,
        "nx": str(nx),
        "ny": str(ny),
    }

    url = ENDPOINT + "?" + urllib.parse.urlencode(params, doseq=True)

    with urllib.request.urlopen(url, timeout=15) as res:
        if res.status != 200:
            raise RuntimeError(f"HTTP 오류: {res.status}")
        body = res.read().decode("utf-8")
        data = json.loads(body)

    header = data["response"]["header"]
    if header.get("resultCode") != "00":
        raise RuntimeError(f"API 오류: {header.get('resultMsg')} ({header.get('resultCode')})")

    items = data["response"]["body"]["items"]["item"]
    return items, base_date, base_time


def sky_text(code):
    return {"1": "맑음", "3": "구름많음", "4": "흐림"}.get(str(code), f"알수없음({code})")


def pty_text(code):
    return {
        "0": "없음",
        "1": "비",
        "2": "비/눈",
        "3": "눈",
        "4": "소나기",
    }.get(str(code), f"알수없음({code})")


def print_today_weather(items):
    today = dt.datetime.now().strftime("%Y%m%d")
    today_items = [x for x in items if x.get("fcstDate") == today]

    if not today_items:
        print("오늘 예보 데이터가 없습니다.")
        return

    # 시간별 데이터 묶기
    by_time = {}
    for it in today_items:
        t = it["fcstTime"]
        by_time.setdefault(t, {})
        by_time[t][it["category"]] = it["fcstValue"]

    # 일최저/일최고
    tmn = next((x["fcstValue"] for x in today_items if x["category"] == "TMN"), None)
    tmx = next((x["fcstValue"] for x in today_items if x["category"] == "TMX"), None)

    print("=== 오늘 날씨(단기예보) ===")
    if tmn is not None or tmx is not None:
        print(f"최저/최고: {tmn if tmn is not None else '-'}°C / {tmx if tmx is not None else '-'}°C")
    print()

    print("시간  기온  강수확률  습도  하늘상태  강수형태")
    print("-" * 46)

    for t in sorted(by_time.keys()):
        row = by_time[t]
        tmp = row.get("TMP", "-")
        pop = row.get("POP", "-")
        reh = row.get("REH", "-")
        sky = sky_text(row.get("SKY", "-"))
        pty = pty_text(row.get("PTY", "-"))
        print(f"{t[:2]}:{t[2:]}  {tmp:>3}°C   {pop:>3}%    {reh:>3}%  {sky:<6}  {pty}")


def main():
    service_key = os.getenv("WEATHER_SERVICE_KEY", "").strip()
    if not service_key:
        print("환경변수 WEATHER_SERVICE_KEY에 공공데이터포털 서비스키를 설정하세요.")
        print("PowerShell 예시:")
        print('$env:WEATHER_SERVICE_KEY="Kfh07Rkb5WAsh0TZ1baGNkuP6C3l78vhmJEz7uV9sZiUPOfVZ0sNo84Ay2m0kK1NTBrR4PC8IccsXZg%2B1v5OhQ%3D%3D"')
        return

    try:
        items, base_date, base_time = request_weather(service_key)
        print(f"발표 기준: {base_date} {base_time}")
        print_today_weather(items)
    except urllib.error.URLError as e:
        print(f"네트워크 오류: {e}")
    except Exception as e:
        print(f"오류: {e}")


if __name__ == "__main__":
    main()