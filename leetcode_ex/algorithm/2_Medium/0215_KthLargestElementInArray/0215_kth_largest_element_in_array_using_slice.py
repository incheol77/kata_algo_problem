import collections
import heapq
from typing import List
import time

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


def main():
    sol = Solution()
    inputs = [[3,2,1,5,6,4], [3,2,3,1,2,4,5,5,6]]
    ks = [2, 4]
    outputs = [5, 4]

    for i in range(len(inputs)):
        start = time.time()
        res = sol.findKthLargest(inputs[i], ks[i])
        end = time.time()
        if outputs[i] == res:
            print("true : ", end-start, " sec")
        else:
            print("false : ", end-start, " sec")


if __name__ == "__main__":
    main()

