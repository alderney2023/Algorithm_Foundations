
import heapq, random


#暴力递归
def arrangeMeeting(lst,timeline_start):
    if not lst or len(lst)==0:
        return 0
    return process(lst, timeline_start)

def process(lst, timeline_start):
    if len(lst) == 0:
        return 0
    max_cnt = 0
    for i in range(len(lst)):
        if lst[i][0]>=timeline_start:
            max_cnt = max(max_cnt,  1 + process(lst[:i]+lst[i+1:], lst[i][1])) 
    return max_cnt


#---------------------------------------------------------------------------------
#贪心算法
def arrangeMeeting2(lst,timeline_start):
    res = 0
    h_end_minheap = []
    for m in lst:
        heapq.heappush(h_end_minheap, (m[1], m))
    while h_end_minheap:
        m = heapq.heappop(h_end_minheap)
        if m[1][0]>=timeline_start:
            res+=1
            #print(timeline_start,m[1])
            timeline_start = m[0]
    return res


#---------------------------------------------------------------------------------

def generateRandomMeetings(meeting_cnt, timeline_start, timeline_end):
    lst = []
    timeline = timeline_end - timeline_start
    for i in range(meeting_cnt):
        a = int((timeline+1) * random.random()) 
        b = int((timeline+1) * random.random()) 
        if a == b:
            b+=1
        else:
            a, b= min(a,b), max(a,b)
        start, end  = timeline_start + a,  timeline_start + b
        #m = meeting(start, end)
        m = (start, end)
        lst.append(m)
    return lst

def main():

    meeting_cnt = 100
    timeline_start = 0
    timeline_end = 250
    lst = generateRandomMeetings(meeting_cnt, timeline_start, timeline_end)

    print("--start--end--")
    for m in lst:
        print(m)
    print("-------------")

    print(arrangeMeeting(lst,timeline_start))
    print(arrangeMeeting2(lst,timeline_start))


if __name__ == "__main__":
    main()