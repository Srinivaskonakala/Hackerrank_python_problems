class Solution(object):
    def addTwoNumbers(self, l1, l2):

        lst1 = []
        lst2 = []

        while l1:
            lst1.append(l1.val)
            l1 = l1.next

        while l2:
            lst2.append(l2.val)
            l2 = l2.next

        num1 = int("".join(map(str, lst1[::-1])))
        num2 = int("".join(map(str, lst2[::-1])))

        total = str(num1 + num2)[::-1]

        dummy = ListNode(0)
        current = dummy

        for digit in total:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
l1=[2,4,3]
l2=[5,6,4]
obj=Solution()
print(obj.addTwoNumbers(l1,l2))

