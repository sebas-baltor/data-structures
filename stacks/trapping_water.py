def trap(height) -> int:
    n = len(height)
    if n < 3:
        return 0

    left, right = 0, n - 1
    max_left, max_right = height[left], height[right]
    trapped_water = 0

    # while left < right:
    #     if height[left] > max_left:
    #         max_left = height[left]
    #     if height[right] > max_right:
    #         max_right = height[right]

    #     min_wall = min(max_left, max_right)

    #     rest_left = min_wall - height[left]
    #     rest_right = min_wall - height[right]

    #     if rest_left > 0:
    #         trapped_water += rest_left
    #     if rest_right > 0:
    #         trapped_water += rest_right

    #     left += 1
    #     right -= 1

    while left < right:
        # Avanzamos el puntero del lado cuyo muro sea menor
        if max_left < max_right:
            left += 1
            # actualizo muro izquierdo
            if height[left] > max_left:
                max_left = height[left]
            else:
                trapped_water += max_left - height[left]
        else:
            right -= 1
            # actualizo muro derecho
            if height[right] > max_right:
                max_right = height[right]
            else:
                trapped_water += max_right - height[right]


    return trapped_water

             
test1 = [0,1,0,2,1,0,1,3,2,1,2,1]
test2 = [4,2,0,3,2,5]
test3 = [0,1,0,2,1,0,1,3,2,1,2,1]

print(trap(test1))  # Output: 6
print(trap(test2))  # Output: 9
print(trap(test3))  # Output: 6


        