# Time Complexity: O(n*mlog(n*m)) n is the max number of nodes, m is the max number of lists - log N for push and pop
# Space Complexity: O(n*m) n is the max number of nodes, m is the max number of lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for head in lists:
            while head:
                heapq.heappush(minHeap, head.val)
                head = head.next

        # Create the merged linked list
        dummy = ListNode(-1)
        current = dummy

        while minHeap:
            val = heapq.heappop(minHeap)
            current.next = ListNode(val)
            current = current.next

        return dummy.next