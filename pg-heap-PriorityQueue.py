# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq

def solution(operations):
    min_heap = []  
    max_heap = [] 
    data = set()   
    idx = 0       
    
    for op in operations:
        command, value = op.split()
        value = int(value)
        
        if command == "I": 
            heapq.heappush(min_heap, (value, idx))  
            heapq.heappush(max_heap, (-value, idx))  
            data.add(idx)
            idx += 1
        elif command == "D":
            if not data:
                continue 
            
            if value == 1:  
                while max_heap:
                    max_val, max_idx = heapq.heappop(max_heap)
                    if max_idx in data:
                        data.remove(max_idx)
                        break
            elif value == -1:  
                while min_heap:
                    min_val, min_idx = heapq.heappop(min_heap)
                    if min_idx in data:
                        data.remove(min_idx)
                        break
    
    max_result, min_result = 0, 0
    while max_heap:
        max_val, max_idx = heapq.heappop(max_heap)
        if max_idx in data:
            max_result = -max_val
            break
    
    while min_heap:
        min_val, min_idx = heapq.heappop(min_heap)
        if min_idx in data:
            min_result = min_val
            break
    
    return [max_result, min_result]