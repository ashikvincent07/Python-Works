class ClosestNumber:

    def solution(self, nums):
        closest_number = nums[0]

        for num in nums:
            if num == 0:
                continue
            if abs(closest_number) == abs(num) and num > closest_number:
                closest_number = num
            elif abs(closest_number) > abs(num):
                closest_number = num

        return closest_number

            
closest_num_instance = ClosestNumber()

nums = [8, 2, -3, 0, 2, -2, 3, 5]

print(closest_num_instance.solution(nums))
