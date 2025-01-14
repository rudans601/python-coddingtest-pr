#https://school.programmers.co.kr/learn/courses/30/lessons/42627
# from collections import deque

# job = []
# pause = deque()
# hard = []
# def solution(jobs):
#     for i, num in enumerate(jobs):
#         job.append([num[0],num[1],i]) # 작업 요청시간, 작업 소요시간, 작업 번호
#     job.sort(key = lambda x : (x[1], x[0],x[2]))
    
#     job_temp = deque(job)
    
#     time = 0
#     for i in range(i[])
#         if time == job_temp[0]
    
    
# print(solution([[0, 3], [1, 9], [3, 5]]))

# 진짜 어려움....
# 정답 코드
import heapq

def solution(jobs):
   
    jobs.sort(key=lambda x: x[0])

    heap = []  
    time, total_time, job_index, completed_jobs = 0, 0, 0, 0
    n = len(jobs)

    while completed_jobs < n:
        while job_index < n and jobs[job_index][0] <= time:
            heapq.heappush(heap, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1

        if heap:
            job_duration, job_request_time = heapq.heappop(heap)
            time += job_duration 
            total_time += (time - job_request_time)  
            completed_jobs += 1
        else:
            time += 1

    return total_time // n

# 테스트 케이스
print(solution([[0, 3], [1, 9], [3, 5]]))  # 출력: 9
