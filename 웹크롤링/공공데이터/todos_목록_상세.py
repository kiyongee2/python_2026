import json
import urllib.request
import urllib.error

URL = "https://jsonplaceholder.typicode.com/todos"

def fetch_todos(url: str):
    with urllib.request.urlopen(url, timeout=10) as res:
        if res.status != 200:
            raise RuntimeError(f"요청 실패: HTTP {res.status}")
        data = json.loads(res.read().decode("utf-8"))
        return data

def print_list(todos, limit: int = 10):
    print(f"=== TODO 목록(요약, 상위 {limit}개) ===")
    for item in todos[:limit]:
        status = "완료" if item["completed"] else "미완료"
        print(f"[{item['id']:>3}] {item['title']} ({status})")

def print_detail(todos, todo_id: int):
    target = next((x for x in todos if x["id"] == todo_id), None)
    print("\n=== TODO 상세 ===")
    if not target:
        print(f"id={todo_id} 항목을 찾지 못했습니다.")
        return
    print(f"id       : {target['id']}")
    print(f"userId   : {target['userId']}")
    print(f"title    : {target['title']}")
    print(f"completed: {target['completed']}")

def main():
    try:
        todos = fetch_todos(URL)
        print_list(todos)

        raw = input("\n상세 조회할 id를 입력하세요 (예: 1): ").strip()
        todo_id = int(raw) if raw else 1
        print_detail(todos, todo_id)

    except urllib.error.URLError as e:
        print(f"네트워크 오류: {e}")
    except ValueError:
        print("숫자 id를 입력하세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()