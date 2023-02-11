class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # 方法一
    if list1 == None or list2 == None:
        return list1 if list1 else list2
    head = ListNode(next=list1)
    result = head
    while list1 and list2:
        if list1.val < list2.val:
            result.next = list1
            list1 = list1.next
        else:
            result.next = list2
            list2 = list2.next
        result = result.next
    result.next = list1 if list1 else list2
    return head.next
    # 方法二 递归
    if list1 == None or list2 == None:
        return list1 if list1 else list2
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    list2.next = mergeTwoLists(list1, list2.next)
    return list2
