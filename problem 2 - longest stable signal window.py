def solve():
    try:
        n = int(input().strip())
        a = [int(x) for x in input().split()]
        k = int(input().strip())
        max_q = deque()
        min_q = deque()
        left = 0
        best_len = 0
        best_start = 1

        for right in range(n):
            val = a[right]
            while max_q and a[max_q[-1]] <= val:
                max_q.pop()
            max_q.append(right)
            while min_q and a[min_q[-1]] >= val:
                min_q.pop()
            min_q.append(right)
            while a[max_q[0]] - a[min_q[0]] > k:
                left += 1
                if max_q[0] < left:
                    max_q.popleft()
                if min_q[0] < left:
                    min_q.popleft()
            curr_len = right - left + 1
            if curr_len > best_len:
                best_len = curr_len
                best_start = left + 1 

        print(f"{best_len} {best_start}")

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
