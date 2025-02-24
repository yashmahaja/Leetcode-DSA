
def insert(intervals, newInterval):
    result = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            # print(result)
            return result + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            # print(result)
            result.append(intervals[i])
        else:
            newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
            # print(result)
        # print(result)
    result.append(newInterval)
    return result

# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
intervals = [[1,3], [6,9]]
# newInterval = [4,8]
newInterval = [2,7]
print(insert(intervals,newInterval))