# PLAN
# 1) find live states
#      - find all states
#      - use nfsmaccepts to check live
# 2) create new fsm
#      - for each state/edge
#        - if dead don't copy
#        - else
#          - copy destinations over if live
#          - if no live destinations
#            don't copy
#      - update accepting
# #! USE LIST COMPREHENSIONS!

def nfsmaccepts(current, edges, accepting, visited):
    if current in visited:
        return None
    elif current in accepting:
        return ""
    else:
        visited.append(current)
        for edge in edges:
            if edge[0] == current:
                for newstate in edges[edge]:
                    foo = nfsmaccepts(newstate, edges, accepting, visited)
                    if foo != None:
                        return edge[1] + foo
        return None

def nfsmtrim(edges, accepting):
    new_accepting = set([])
    pseudo_accepting = set([])
    for edge in edges:
        for state in accepting:
            if state in edges[edge]:
                new_accepting.update([state])
        if nfsmaccepts(edge[0], edges, accepting, []):
            pseudo_accepting.update(set([edge[0]]))
    pseudo_accepting.update(set(new_accepting))

    new_edges = {}
    for edge in edges:
        for state in edges[edge]:
            if edge[0] in pseudo_accepting and state in pseudo_accepting:
                if edge not in new_edges:
                    new_edges[edge] = [state]
                else:
                    new_edges[edge].append(state)
    return new_edges, list(new_accepting)



# edges = {
#     (1,'a'): [2],
#     (2,'b'): [3],
#     (3,'c'): [4]
# }

# accepting = [4]

# edges = { (1,'a') : [1] ,
#            (1,'b') : [2,5] ,
#            (2,'b') : [3] ,
#            (3,'b') : [4] ,
#            (3,'c') : [2,1,4] } 
# accepting = [ 2 ] 

edges = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , }

(new_edges3, new_accepting3) = nfsmtrim(edges,[3,6]) 
print new_edges3 == {(1, 'a'): [1], (1, 'b'): [2], (2, 'b'): [3]}
print new_accepting3 == [3]
print nfsmtrim(edges, [3,6])