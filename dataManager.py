from pathlib import Path
import json

class Datamanager:
    def __init__(self):
        self.path = "./data.json"
        self.cache = []
        
        file_path = Path(self.path)
        # check if ./data.json exists
        if file_path.exists():
            # if it exist, read it and save it to self.cache
            print("path exist")
            with open(self.path, 'r') as file:
                self.cache = json.load(file)
        else: 
            # create it if it does not
            self.cache = []
            self.saveToFile()
            print('data.json created')
    #CRUD
    def createTodo(self, dataSet):
        # adds the data into the json list
        self.cache.append(dataSet)
        # saves the data to localstorage
        self.saveToFile()
        
    def getAllTodo(self):
        # returns the entire list
        return self.cache

    def updateOneTodo(self, index, data):
        # replaces one of the data in the list by index
        if 0 <= index < len(self.cache):
            self.cache[index] = data
            self.saveToFile()
        else:
            print("invalid index")

    def deleteOneTodo(self, index):
        # deletes one of the data in the list by index
        if 0 <= index < len(self.cache):
            del self.cache[index]
            self.saveToFile()
        else:
            print("invalid index")
    def deleteAllTodo(self):
        self.cache = []
        self.saveToFile()   
        return self.cache
            
    def saveToFile(self):
        with open(self.path, 'w') as file:
            json.dump(self.cache, file, indent=4)
        print('data saved to file')