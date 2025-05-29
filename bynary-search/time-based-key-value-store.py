import math
class TimeMap:

    def __init__(self):
        self.timemaps = []
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        left,right=0,len(self.timemaps)-1
        
        if key == 'TimeMap': return None
        if len(self.timemaps) == 0:
            newValues = [key,value if value else None, timestamp]
            self.timemaps.append(newValues)
            return None


        while left<=right:
            
            middle=round((right+left)/2)
            selfKey = self.timemaps[middle][0]
            selfTimestamp = self.timemaps[middle][2]
            
            if selfTimestamp < timestamp:
                left = middle
            else:
                right = middle

            middleToFind = middle-1 if middle != 0 else middle
            timestampToCompare = self.timemaps[middleToFind][2]
            keyToCompare = self.timemaps[middleToFind][0]

            if right == left and timestamp >= timestampToCompare  and ( keyToCompare == key or keyToCompare != key):
                newValues = [key,value if value else None, timestamp]
                self.timemaps.insert(middle+1,newValues)
                return None

            if selfKey == key:
                if selfTimestamp < timestamp:
                    left+= 1
                if selfTimestamp > timestamp:
                    right -= 1


    def get(self, key: str, timestamp: int) -> str:
        left,right=0,len(self.timemaps)-1
        
        while left<=right:
            middle=math.ceil(right+left/2)
            selfTimestamp = self.timemaps[middle][2]
            if self.timemaps[middle][0] != key:
                continue

            if selfTimestamp == timestamp or right == 0:
                return self.timemaps[middle][1]
            
            if timestamp > selfTimestamp:
                left = middle
            else:
                right = middle

            if right - left <= 1:
                if self.timemaps[right][0] == key and self.timemaps[right][2] == timestamp:
                    return self.timemaps[right][1]
                else:
                    if self.timemaps[left][0] == key and self.timemaps[left][2] > timestamp:
                        return ""
                    return self.timemaps[left][1]
                break
        



# ejecutions = ["TimeMap","set","get","get","set","get","get"]
# values=[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]

ejecutions = ["TimeMap","set","set","get","get","get","get","get"]
values = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

obj = TimeMap()
for i in range(len(ejecutions)):
    if ejecutions[i] == "TimeMap":
        obj.set(
            'TimeMap', None,None
        )
    elif ejecutions[i] == "set":
        print(obj.set(values[i][0], values[i][1], values[i][2]))
    elif ejecutions[i] == "get":
        print(obj.get(values[i][0], values[i][1]))
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)