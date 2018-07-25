# For example, this non-deterministic machine ...
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 2],
          (4, 'c') : [5] }
accepting = [5] 
# ... accepts exactly one string: "abc". By contrast, this
# non-deterministic machine: 
edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }
accepting2 = [2] 
# ... accepts no strings (if you look closely, you'll see that you cannot
# actually reach state 2 when starting in state 1). 

# Hint #1: This problem is trickier than it looks. If you do not keep track
# of where you have been, your procedure may loop forever on the second
# example. Before you make a recursive call, add the current state to the
# list of visited states (and be sure to check the list of visited states
# elsewhere). 
#
# Hint #2: (Base Case) If the current state is accepting, you can return
# "" as an accepting string.  
# 
# Hint #3: (Recursion) If you have an outgoing edge labeled "a" that
# goes to a state that accepts on the string "bc" (i.e., the recursive call
# returns "bc"), then you can return "abc". 
#
# Hint #4: You may want to iterate over all of the edges and only consider
# those relevant to your current state. "for edge in edges" will iterate
# over all of the keys in the mapping (i.e., over all of the (state,letter)
# pairs) -- you'll have to write "edges[edge]" to get the destination list. 

def nfsmaccepts(current, edges, accepting, visited=[]):
    if current in visited:
        return None
    elif current in accepting:
        return ""
        # for edge in edges:
        #     if edge[0] == current:
        #         return edge[1]
    else:
        visited.append(current)
        for edge in edges:
            if edge[0] == current:
                for newstate in edges[edge]:
                    foo = nfsmaccepts(newstate, edges, accepting, visited)
                    if foo != None:
                        return edge[1] + foo
        return None
                


# This problem includes some test cases to help you tell if you are on
# the right track. You may want to make your own additional tests as well.
# print "Test 1: " + str(nfsmaccepts(1, edges, accepting, []) == "abc") , nfsmaccepts(1, edges, accepting, [])
# print "Test 2: " + str(nfsmaccepts(1, edges, [4], []) == "ab") 
# print "Test 3: " + str(nfsmaccepts(1, edges2, accepting2, []) == None) 
# print "Test 4: " + str(nfsmaccepts(1, edges2, [1], []) == "")

def nfsmtrim(edges, accepting):
    pseudo_accepting = set([])
    for edge in edges:
        if nfsmaccepts(edge[0], edges, accepting, []):
            pseudo_accepting.update(set([edge[0]]))
    pseudo_accepting.update(set(accepting))

    new_edges = {}
    for edge in edges:
        for state in edges[edge]:
            if edge[0] in pseudo_accepting and state in pseudo_accepting:
                if edge not in new_edges:
                    new_edges[edge] = [state]
                else:
                    new_edges[edge].append(state)
    return (new_edges, accepting)

# We have included a few test cases, but you will definitely want to make
# your own. 

edges1 = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , }
accepting1 = [ 1 ] 

(new_edges1, new_accepting1) = nfsmtrim(edges1,accepting1) 
print new_edges1 == {(1, 'a'): [1]}
print new_accepting1 == [1] 

(new_edges2, new_accepting2) = nfsmtrim(edges1,[]) 
print new_edges2 == {}
print new_accepting2 == [] 

(new_edges3, new_accepting3) = nfsmtrim(edges1,[3,6]) 
print new_edges3 == {(1, 'a'): [1], (1, 'b'): [2], (2, 'b'): [3]}
print new_accepting3 == [3]



edges4 = { (1,'a') : [1] ,
           (1,'b') : [2,5] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (3,'c') : [2,1,4] } 
accepting4 = [ 2 ] 
(new_edges4, new_accepting4) = nfsmtrim(edges4, accepting4) 
print new_edges4 == { 
  (1, 'a'): [1],
  (1, 'b'): [2], 
  (2, 'b'): [3], 
  (3, 'c'): [2, 1], 
}
print new_accepting4 == [2]



