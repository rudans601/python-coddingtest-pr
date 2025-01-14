# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     bridge = deque()
#     bridge_weight = 0
#     time = 0
    
#     while truck_weights:
#         now = truck_weights.pop()
#         if bridge_length > len(bridge) and now + bridge_weight <= weight:
#             bridge.append(now)
#             bridge_weight += now
#         time += 1
        
#         if time 
    
#     return time

# 정답 코드
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # 다리 위 상태 (0은 빈 공간)
    bridge_weight = 0  # 현재 다리 위 총 무게
    time = 0  # 시간

    truck_weights = deque(truck_weights)  # 트럭 대기열을 deque로 변환

    while bridge:
        time += 1  # 1초 증가
        bridge_weight -= bridge.popleft()  # 다리 앞에서 트럭 이동

        if truck_weights:
            # 다음 트럭이 다리 위로 올라갈 수 있는지 확인
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)  # 트럭이 못 올라가면 빈 공간 유지

    return time