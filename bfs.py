from collections import deque
# 通过散列来存储图信息
graph={}
graph["you"] = ["a","b","c"]
graph["b"] = ["an","pe"]
graph["a"] = ["pe"]
graph["c"] = ["th","jo","m"]
graph["an"] = []
graph["pe"] = []
graph["th"] = []
graph["jo"] = []
def search(name):
    search_queue = deque()
    search_queue +=graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller")
                return True
            else:
                search_queue +=graph[person]#如果不是销售商将这个人的朋友都加入搜索队列
        return False


def person_is_seller(name):
    return name[-1] == 'm'

print(search("you"))
