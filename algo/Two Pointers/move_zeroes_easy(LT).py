def move_zeros(nums):
    first_pointer = 0
    second_pointer = 1
    while second_pointer < len(nums):
        if nums[first_pointer] == 0:
            if nums[second_pointer] != 0:
                nums[second_pointer], nums[first_pointer] = nums[first_pointer], nums[second_pointer]
                first_pointer += 1
                second_pointer += 1
            else:
                second_pointer += 1
        else:
            first_pointer += 1
            second_pointer += 1       
    return nums    
        
                        
    pass
    # r = len(nums)
    # for i in range(r):
    #     if nums[i] == 0:
    #         if nums[pointer] != 0:
    #             nums[pointer], nums[i] = nums[i], nums[pointer]
    #     pointer += 1    
            

nums = [0,1,0,3,12]
print(move_zeros(nums))