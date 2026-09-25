def solve():
    try:
        line = input().strip()
        while not line:
            line = input().strip()
        n = int(line)
        intervals = []
        for _ in range(n):
            parts = input().split()
            while len(parts) < 2: 
                parts.extend(input().split())
            start, end = int(parts[0]), int(parts[1])
            intervals.append((start, end))
        intervals.sort(key=lambda x: x[0])
        merged = []
        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        for start, end in merged:
            print(f"{start} {end}")

    except EOFError:
        pass

if __name__ == "__main__":
    solve()
