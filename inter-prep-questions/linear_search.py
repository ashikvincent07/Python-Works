class LinearSearch:

    def solution(self, arr, element):
        is_present = False
        i = 0

        while i < len(arr):

            if arr[i] == element:
                is_present = True
                break

            i += 1

        print(is_present)

lsearch_instance = LinearSearch()

lsearch_instance.solution([2,3,4,1,7,8,9,34], 14)
