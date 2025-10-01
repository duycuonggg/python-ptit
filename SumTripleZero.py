for t in range(int(input())):
    n = int(input())
    # sorted tạo ra 1 mảng mới và không phụ thuộc list như sort
    arr = sorted(int(i) for i in input().split())
    count = 0
    # lặp đến vị trí thứ 3 bên phải cách 2 vị trí cuối
    for i in range(n-2):
        # arr là số cố định tìm 2 con trỏ l(đầu mảng), r(cuối mảng) sao cho tổng l , r = arr
        l, r = i+1, n-1
        while l < r:
            temp = arr[i] + arr[l] + arr[r]
            # nếu tổng = 0 đếm count và chuyển con trỏ sang trái tìm số tiếp theo
            if temp == 0:
                count += 1
                l += 1
            # nếu tổng < 0 tăng l
            elif temp < 0:
                l += 1
            # nếu tổng > 0 giảm r
            else:
                r -= 1
    print(count)