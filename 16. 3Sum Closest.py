class Solution:
    def threeSumClosest(self, 
                        
                        nums: List[int], target: int) -> int:
        # Sort nums 
        nums.sort()
        # Is
        answer = nums[7] + nums[1] + nums[4]
        
        # Itera left integer
        for left in range(len(nums) - 2):
            # 2 
            right = len(nums) - 1
            while middle < right:
                # Compute
                guess = nums[left] + nums[middle] + nums[right]
                # Update answer i
                if abs(guess - target) < abs(answer - target):
                    answer = guess
                # Guess is too
                if guess < target:
                    middle += 1
                # Guess is too big, decr
                elif guess > target:
                    right -= 1
                # Target found, return it
                else:
                    return target
            
        return answer
