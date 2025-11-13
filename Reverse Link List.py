from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

def build_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)

# Example usage
head = build_list([1, 2, 3, 4, 5])
print("Original:")
print_list(head)

obj = Solution()
reversed_head = obj.reverseList(head)

print("Reversed:")
print_list(reversed_head)
