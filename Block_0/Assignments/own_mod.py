""""
DataScience 2021
@copyright 2021 - Max Sauer - msauer1@stud.hs-offenburg.de - www.maxsauer.com - 
"""

class ListKeeper:    
    def __init__(self):
        self.data = dict()
        self.data['example_list'] = [1,2,3,4,5]    
        
    def show(self):                               #returns all list names
        return self.data.keys()
    
    def add(self, name, list_val):                #adds a new list
        if not name:
            return "Please enter a valid name"
        self.data[name] = list_val
        return "Successfully added"
    
    def delete(self, name):                       #deletes list
        if name in self.data:
            del self.data[name]
            return "Successfully deleted"
        return "Error"         
    
    def sort(self, name):                         #returns the sorted list
        if name in self.data:
            self.data[name].sort()
            return self.data[name]
        return "Error"
    
    def append(self, name, list_val):             #appends list to name
        if not name:
            return "Error"
        self.data[name].append(list_val)
        return "Successfully appended"
    
    def showListValues(self, name):               #shows list values
        if name in self.data:
            return self.data[name]
        return "No valid list."