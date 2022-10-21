'''
Implement a group_by_owners function that:

    > Accepts a dictionary containing the file owner name for each file name.
    > Returns a dictionary containing a list of file names for each owner name, in any order.

For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

-----------------|-------------------
Difficulty: Easy
Duration: 10 min

Python 3.7.4, Base Test:

def group_by_owners(files):
    return None

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))
'''


def group_by_owners(files):
    result = {}
    
    for key in files.keys():
      curr_value = files[key]
      
      if not curr_value in result:
        result[curr_value] = []
        
      result[curr_value].append(key)
      
    return result

if __name__ == "__main__":    
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }   
    print(group_by_owners(files))