

class Node:
    def __init__(self, keyword=None, data=None, _next=None, previous=None):
        self.keyword = keyword
        self.data = data
        self.next = _next
        self.previous = previous

    def __str__(self):
        ret = ""
        if self.keyword:
            ret += f"{self.keyword} "
        if self.next:
            ret += f"{self.next.__str__()} "
        return ret
