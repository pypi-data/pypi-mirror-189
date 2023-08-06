class Pickson:
    
    """This is a simple module for converting data to JSON or a pickle.
    If you wish to save an object, use the pickle option."""
    
    
    def __init__(self, name:str,  data:bytes or str, data_type: str, location: str = "."):
        import json, pickle, os
        self.name = name
        self.data = data
        self.data_type = data_type
        self.location = location
        self.json = json
        self.pickle = pickle
    
    def save_data(self):
        
        if self.data_type == "json":
            
            saving = self.json.dumps(self.data)
            file = open(self.location + "/" + self.name + ".json", "w")
            file.write(saving)
            file.close()
            
        elif self.data_type == "pickle":
         
            with open(self.name + ".pickle", "wb") as file:
                    self.pickle.dump(self.data, file)
                    
        else:
            print("Invalid data type. Cannot save. Must be JSON or Pickle")
    
    def get_data(self):
        
        if self.data_type == "json":
            json_data = open(self.name + ".json", "r")

            json_read = json_data.read()
            data = self.json.loads(json_read)
            json_data.close()
            return data
        
        elif self.data_type == "pickle":
            with open(self.name + ".pickle", "rb") as r:
                data = self.pickle.load(r)
                
            return data

    def convert_to_json(self):
        pass
    
    def convert_to_pickle(self):
        pass
    