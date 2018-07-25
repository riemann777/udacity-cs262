# def cfgempty(grammar,symbol,visited):
    # if symbol not in [ rwr[0] for rwr in grammar ]:
    #      return [ symbol ]
    # else:
    #     visited.append(symbol)
    #     for rwr in grammar:
    #         if symbol not in visited and symbol == rwr[0]:
    #             for new_symbol in rwr[1]:
    #                 foo = cfgempty(grammar,new_symbol,visited)
    #                 return foo
def cfgempty(grammar,symbol,visited):
    if symbol in visited:
        return None
    elif not any([ rule[0] == symbol for rule in grammar ]):
        return [ symbol ]
    else:
        new_visited = visited + [symbol]

        for rwr in [ rule[1] for rule in grammar if rule[0] == symbol ]:
            if all([ None != cfgempty(grammar,new_symbol,new_visited) for new_symbol in rwr]):
                result = []
                for new_symbol in rwr:
                    result = result + cfgempty(grammar,new_symbol,new_visited)
                return result
    return None

                    
# We have provided a few test cases for you. You will likely want to add
# more of your own. 

grammar1 = [ 
      ("S", [ "P", "a" ] ),           
      ("P", [ "S" ]) ,               
      ] 
                        
print cfgempty(grammar1,"S",[])# == None 

grammar2 = [
      ("S", ["P", "a" ]),             
      ("S", ["Q", "b" ]),             
      ("P", ["P"]), 
      ("Q", ["c", "d"]),              
      ] 

print cfgempty(grammar2,"S",[])# == ['c', 'd', 'b']


# grammar3 = [  # some Spanish provinces
#         ("S", [ "Barcelona", "P", "Huelva"]),
#         ("S", [ "Q" ]),
#         ("Q", [ "S" ]),
#         ("P", [ "Las Palmas", "R", "Madrid"]),
#         ("P", [ "T" ]),
#         ("T", [ "T", "Toledo" ]),
#         ("R", [ ]) ,
#         ("R", [ "R"]), 
#         ]

# print cfgempty(grammar3,"S",[]) == ['Barcelona', 'Las Palmas', 'Madrid', 'Huelva']
