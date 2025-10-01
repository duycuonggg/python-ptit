def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx+n])); idx += n
        
        # tìm 3 min và 2 max
        min1 = min2 = min3 = float('inf')
        max1 = max2 = -float('inf')
        
        for x in arr:
            # update min
            if x < min1:
                min3 = min2
                min2 = min1
                min1 = x
            elif x < min2:
                min3 = min2
                min2 = x
            elif x < min3:
                min3 = x
            
            # update max
            if x > max1:
                max2 = max1
                max1 = x
            elif x > max2:
                max2 = x
        
        # so sánh 2 trường hợp
        res = min(min1 + min2 + min3, min1 + max1 + max2)
        results.append(res)
    
    for r in results:
        print(r)
