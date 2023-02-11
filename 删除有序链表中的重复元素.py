class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    # 方法一，迭代
    if head is None:
        return
    p = head
    while p.next != None:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head
    # 方法二，递归
    if head == None or head.next == None:
        return head
    head.next = deleteDuplicates(head.next)
    return head.next if head.val == head.next.val else head
