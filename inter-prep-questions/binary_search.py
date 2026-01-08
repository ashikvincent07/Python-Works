class BinarySearch:

    def solution(self, arr, element):
        arr.sort()
        is_present = False
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if element == arr[mid]:
                is_present = True
                break
            
            elif arr[mid] > element:
                high = mid -1

            else :
                low = mid + 1

        print(is_present)
    

bsearch_instance = BinarySearch()

bsearch_instance.solution([3, 89, 4, 6, 9, 45, 32], 88)
bsearch_instance.solution([3, 89, 4, 6, 9, 45, 32], 89)