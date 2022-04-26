class ParsingNode:
    def __init__(self, keyword=None, name=None, lst=None, _next=None, previous=None):
        self.keyword = keyword
        self.name = name
        self.lst = lst
        self.next = _next
        self.previous = previous

    def __str__(self):
        ret = ""
        if self.keyword:
            ret += f"{self.keyword} "
        if self.name:
            ret += f"<{self.name}> "
        if self.lst:
            ret += f"{self.lst} "
        if self.next:
            ret += f"{self.next.__str__()} "
        return ret