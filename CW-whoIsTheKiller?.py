# Who is the killer?
# Some people have been killed!
# You have managed to narrow the suspects down to just a few. Luckily, you know every person who those suspects have seen on the day of the murders.

# Task.
# Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:

# {'James': ['Jacob', 'Bill', 'Lucas'],
#  'Johnny': ['David', 'Kyle', 'Lucas'],
#  'Peter': ['Lucy', 'Kyle']}
# and also a list of the names of the dead people:

# ['Lucas', 'Bill']
# return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'

# FUNDAMENTALSDICTIONARYDATA STRUCTURESLISTSOBJECTS

# powered by


def killer(suspect_info, dead):
    
    
    def suspect_conviction(suspect):
        
        death_toll = len(dead)
        
        for victim in dead:
            if victim in suspect_info[suspect]:
                death_toll -=1
                
        if death_toll >0:
            return False
        else:
            return True
    killers = []    
    for suspect in list(suspect_info.keys()):
        if suspect_conviction(suspect):
            killers.append(suspect)
            
    return killers[0]