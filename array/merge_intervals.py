from typing import List

# def bynaryJoin(start:int,end:int,intervals,steps,actualSteps=0):
#     if(start>=end or actualSteps >= steps): return
#     middle=round((start+end)/2)
#     if middle + 1 <= end and intervals[middle][1] >= intervals[middle+1][0]:
#         intervals[start][1] = intervals[end][1]
#         del intervals[end]
#             # return intervals
#         middle -= 1
#         actualSteps += 1

#     bynaryJoin(start,middle,intervals,steps,actualSteps)
#     bynaryJoin(middle+1,end,intervals,steps,actualSteps)

#     print(intervals)

# def merge(intervals: List[List[int]]) -> List[List[int]]:
#         start,end,steps = 0,len(intervals)-1,round(len(intervals)/2)
#         if steps == 0: return intervals

#         bynaryJoin(start,end,intervals,steps)
#         print('its supose to ve the las interval',intervals)


                    # return intervals


# merge([[1,3],[2,6],[8,10],[15,18],[17,20]])


def cursorsImplementation(intervals: List[List[int]]) -> List[List[int]]:
    cursor,end=1,len(intervals)-1

    if end == 0: return
    while(cursor<=end):
        # print(f'cursor: {cursor}, end: {end}, intervals: {intervals} cursor-1: {cursor-1}')
        if intervals[cursor-1][1] >= intervals[cursor][0]:
            # print(f'overlap cursor: {cursor}, end: {end}, intervals: {intervals}')
            intervals[cursor-1][1] = intervals[cursor][1]
            del intervals[cursor]
            end-=1

        cursor+=1

    return intervals

print(cursorsImplementation([[1,3],[2,6],[8,10],[15,18],[17,20]]))