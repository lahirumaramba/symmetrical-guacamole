class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

list1 = ListNode(10)
list1.next = ListNode(25)
list1.next.next = ListNode(45)

list2 = ListNode(10)
list2.next = ListNode(12)
list2.next.next = ListNode(14)

list3 = ListNode(2)
list3.next = ListNode(4)
list3.next.next = ListNode(5)

list4 = ListNode(22)
list4.next = ListNode(44)
list4.next.next = ListNode(55)

def print_list(head):
    while head:
        print head.val,
        head = head.next
    print("")

print_list(list1)
print_list(list2)
print_list(list3)
print_list(list4)

def merge_2_lists(head_a, head_b):
    point = head = ListNode(0)

    while head_a and head_b:
        if head_a.val < head_b.val:
            point.next = head_a
            point = point.next
            head_a = head_a.next
            continue
        point.next = head_b
        point = point.next
        head_b = head_b.next

    if head_a:
        point.next = head_a

    if head_b:
        point.next = head_b

    return head.next

#list_merged = merge_2_lists(list1, list2)

#print("------")
#print_list(list_merged)
#print("------")

lists = [list1, list2, list3, list4]

def merge_k_lists(lists):
    while len(lists) != 1:
        merged = merge_2_lists(lists.pop(), lists.pop())
        lists.append(merged)

    return lists[0]

list_merged = merge_k_lists(lists)

print("------")
print_list(list_merged)
print("------")
