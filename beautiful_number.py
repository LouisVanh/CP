test_case_count = int(input())
for _ in range(test_case_count):
    x = int(input())
    # need to find the sum of the digits
    # but also keep track off the pos of the largest
    def keep_swapping_until_beautiful(number,swaps):
        sum_of_digits = 0
        highest_digit = (-1, 0)
        for i in range(len(str(number))-1, -1, -1): # iterate backwards to avoid infinite stuck at 111111111111111
            digit = str(number)[i]
            sum_of_digits += int(digit)
            if(highest_digit[0] < int(digit)):
                # we found the highest, for the first time
                highest_digit = (int(str(number)[i]), i)
                if(digit == '9' and i>0):
                    # this is definitely the highest, and its not just the number 9 (multiple digits)
                    # we can thus break out of the loop
                    break
        
        if(sum_of_digits < 10):
            print(swaps)
            return
        
        else:
            # no beautiful number yet
            # we have now found the highest digit, we intend to make it 0 or 1 (if its the first)
            if(highest_digit[1] == 0): # first digit, make it a one
                lst = list(str(number))
                lst[highest_digit[1]] = '1'
                new_x = ''.join(lst)
            else:
                lst = list(str(number))
                lst[highest_digit[1]] = '0'
                new_x = ''.join(lst)
            
            keep_swapping_until_beautiful(int(new_x), swaps+1)
    
    keep_swapping_until_beautiful(x,0)

