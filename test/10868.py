import sys          # 아래의 함수를 쓰기 위한 라이브러리
input = sys.stdin.readline  # 입력을 한 줄씩 읽어주는 함수
MAX = sys.maxsize   # MAX를 정수 최댓값으로 설정

# 정수 N,M과 N개의 정수 입력 받기
N, M = map(int, input().split())
arr = [0] + [int(input()) for _ in range(N)]

# 펜윅 트리 모든 값 MAX로 초기화
tree_min_from_start = [MAX] * (N + 1)
tree_min_from_end = [MAX] * (N + 1)

# 시작부터 끝까지의 최소값을 업데이트
def update_tree_from_start(index, value):
    while index <= N:
        tree_min_from_start[index] = min(tree_min_from_start[index], value)
        index += (index & -index)

# 끝에서 시작까지의 최소값을 업데이트
def update_tree_from_end(index, value):
    while index > 0:
        tree_min_from_end[index] = min(tree_min_from_end[index], value)
        index -= (index & -index)

# 주어진 범위 [start, end] 내의 최소값 찾기
def find_range_min(start, end):
    result = MAX

    # 왼쪽에서 오른쪽으로 최소값 찾기
    pre = start
    cur = pre + (pre & -pre)
    while cur <= end:
        result = min(result, tree_min_from_end[pre])
        pre = cur
        cur = pre + (pre & -pre)
    result = min(result, arr[pre])

    # 오른쪽에서 왼쪽으로 최소값 찾기
    pre = end
    cur = pre - (pre & -pre)
    while cur >= start:
        result = min(result, tree_min_from_start[pre])
        pre = cur
        cur = pre - (pre & -pre)

    return result

# 트리 업데이트
for i in range(1, N + 1):
    update_tree_from_start(i, arr[i])
    update_tree_from_end(i, arr[i])

# 쿼리 처리 및 결과 출력
for _ in range(M):
    start, end = map(int, input().split())
    print(find_range_min(start, end))

