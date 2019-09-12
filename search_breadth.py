# Algorithmic efficiency - O(V + E)

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def breadth_first_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_seelling_mango(person):
                print(f"{person} is selling mango")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False 
    
def is_seelling_mango(person):
    if person.endswith("m"):
        return True
    return False

def main():
    breadth_first_search("you")

if __name__ == "__main__":
    main() 
