class MergeInterval:

    def solution(self, intervals):
        intervals.sort(key = lambda x: x[0]) # sort based on first element

        merge_interval = [intervals[0]] # set merge interval with first interval list

        for interval in intervals[1:]:
            if interval[0] <= merge_interval[-1][1]: #check first element of interval lt or eq to last interval sec element of marge_list
                merge_interval[-1][1] = max(merge_interval[-1][1], interval[1]) # last inteval sec value set as max 
                                                                                #(last element sec value of marge elemnet or interval sec value)
            else:
                merge_interval.append(interval) # append interval
            
            
        print(merge_interval)
       
    

merge_interval_instance = MergeInterval()

intervals = [[4, 8], [1, 8], [9 , 10], [11, 15]]

merge_interval_instance.solution(intervals)





            
