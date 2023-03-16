# stack by using LinkList

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class Stack:

    def __init__(self):

        self.top=None
        self.n=0
        self.ref=None

    def __str__(self):
        if self.top:
            result=""
            travle=self.top
            while travle:
                result+=f"|{travle.data}|\n"
                travle=travle.next
            return result
        return "None"
    def __del__(self):
        return True

    def isempty(self):
        return self.top == None

    def push(self,value):
        node=Node(value)
        node.next=self.top
        self.top=node
        self.n+=1
        return 

    def pop(self):

        if not self.isempty():
            value=self.top.data
            self.top=self.top.next
            self.n-=1
            return value
        raise ValueError("StackIsEmpty")

    def peak(self):

        if not self.isempty():
            return self.top.data
            # return True
        raise ValueError("StackIsEmpty")

    def stack_reverse(self):
        """reversing stack in-place"""

        if not self.isempty():
            travle=self.top
            second=travle.next
            while second:
                c=second.next
                second.next=travle
                travle,second=second,c
            self.top.next=None
            self.top=travle
            return True
        raise ValueError("StackIsEmpty")
    
    def custom_travle(self):
        if self.top:
            result=""
            travle=self.top
            while travle:
                result=travle.data+result
                travle=travle.next
            return result
        # print()
        return ""
    
    def undo(self):
        if self.ref == None:
            self.ref=Stack()
        if self.top:
            self.ref.push(self.pop())
            return self.custom_travle()
        return self.custom_travle()

    def redo(self):
        if self.ref.top:
            self.push(self.ref.pop())
            return self.custom_travle()
        return self.custom_travle()

    def undo_old(self):
        if self.top:
            self.ref=self.top
            self.top=self.top.next
            self.n-=1
            return self.custom_travle()
        return self.custom_travle()

    def redo_old(self):
        if self.ref:
            self.ref.next=self.top
            self.top=self.ref
            self.n+=1
            self.ref=None
            return self.custom_travle()
        return self.custom_travle()

    def travle(self):
        if self.top:
            tra=self.top
            result=''
            while tra:
                result+=tra.data
                tra=tra.next
            return result
        return "Stack Empty"

    def string_rev(self,value):
        obj=Stack()
        for i in value:
            obj.push(i)
        print(obj.travle())
        del obj
        return True


"""def string_rev(value):
    obj=Stack()
    for i in value:
        obj.push(i)
    print(obj.travle())
    return True
"""
# def undo_redo(string,pattern):
#     obj=Stack()
#     for i in string:
#         obj.push(i)

# s=Stack()

# string="bhujang"
# for i in string:
#     s.push(i)
# print(s)

# s.undo()
# s.undo()
# s.redo()
# s.redo()

