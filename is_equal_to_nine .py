def is_equal_to_nine(arr):
    new_arr = []
    n = len(arr)
    for i in range(n):
        for j in range(n-1 , -1 ,-1):
            print(arr[j], arr[i])
            if arr[i] + arr[j] == 9:
                res = [arr[i] , arr[j]]
                new_arr.append(res)
            if i - j == -1 :
                break
            i+=1
        break

    return new_arr
    
arr = [1,3,4,5,6,9]
print(is_equal_to_nine(arr))










