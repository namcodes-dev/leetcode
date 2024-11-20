def maxArea(heights):

    l = 0
    r = len(heights) - 1
    result = 0
    while l < r:
        area = (r-l) * min(heights[l], heights[r])
        result = max(area, result)

        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return result

print(maxArea([1,7,2,5,4,7,3,6]))