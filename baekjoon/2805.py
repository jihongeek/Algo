from sys import stdin

n,m = map(int,stdin.readline().strip().split())
trees = list(map(int,stdin.readline().strip().split()))

start = 0
end = 1000000000

while start + 1 < end:
  mid = (start + end) // 2
  tree_sum = 0
  for tree in trees:
    tree_sum += max(0, tree - mid)
  if tree_sum >= m:
    start = mid
  else:
    end = mid
print(start)