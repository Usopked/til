from sll import Linked_list

def get_data(msg):
    print(msg, end = ">>> ")
    data = input()
    return int(data) if data.isdigit() else data

my_list = Linked_list()

while True:
    menu = """
-----------------------
실행할 명령어를 선택하세요.

[0] 연결 리스트의 상태 출력
[1] 처음에 노드 추가   [2] 끝에 노드 추가      [3] 노드 검색
[4] 첫 노드 꺼내기     [5] 마지막 노드 꺼내기  [6] 특정 위치에 노드 삽입
[7] 노드 삭제         [8] 연결 리스트 뒤집기
[9] 끝내기

"""
    print(menu, end=" >>> ")
    command = int(input())
    print("-----------------------")
    print()

    if command == 0:
        print(my_list)
    elif command == 1:
        my_list.appendleft(get_data("추가할 값(정수, 문자)을 입력하세요."))
    elif command == 2:
        my_list.append(get_data("추가할 값(정수, 문자)을 입력하세요."))
    elif command == 3:
        data = get_data("검색할 값을 입력하세요.")
        if data in my_list:
            print(f"{data}(이)가 리스트에 있습니다.")
        else:
            print(f"{data}(이)가 리스트에 없습니다.")
    elif command == 4:
        print(my_list.popleft())
    elif command == 5:
        print(my_list.pop())
    elif command == 6:
        index = get_data("값을 추가할 인덱스를 입력하세요.")
        my_list.insert(index, get_data("추가할 값을 입력하세요."))
    elif command == 7:
        data = get_data("삭제할 값을 입력하세요.")
        if my_list.remove(data):
            print(f"{data}(을)를 정상적으로 삭제했습니다.")
        else:
            print(f"{data}(이)가 리스트에 없습니다.")
    elif command == 8:
        my_list.reverse()
        print("리스트를 뒤집었습니다.")
    elif command == 9:
        break
