def biggest_alternating(nums):
    nums.append(-nums[-1]) #last element is fransition

    sub_nums =[]
    extreme_num = -float("inf")
    in_positives = nums[0] > 0

    for num in nums:
        to_negatives = in_positives and num < 0
        to_positives = (not in_positives )and num > 0

        if egative and to_positives:
            in_positives = not in_positives
            sub_nums.append(extreme_num)
            extreme_num = float("mn")
            
        extreme_num = max(extreme)
    return sub_nums

def main():
    

    stcase= int(input())
    for _ in range(num_tes)
        length = int(input())
        nom= list(map(int, input().split(g))
        print(sum(biggest_alternating(nuo)))


main()