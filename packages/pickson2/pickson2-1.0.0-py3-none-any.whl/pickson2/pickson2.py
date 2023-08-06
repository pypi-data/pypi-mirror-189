class Pickson:
    
    """This is a package to do the following:
        - Save files as either JSON or Pickled file.
        - Get the data as either JSON and/or pickled file.
    """
    import pickle, json, os, click
    name = "default"
    data = []
    data_type = "json"
    folder = "."

    def __init__(self):
        pass
        
       
    @classmethod
    def save_data(cls, name: str, data:object or str or bytes, data_type:str, folder: str = ".") -> None:
        
        cls.name = name
        cls.data = data
        cls.data_type = data_type
        cls.folder = folder
        
        if cls.data_type == "json":
            
            saving = cls.json.dumps(cls.data)
            if cls.folder == ".":
                file = open(cls.name + ".json", "w")
            else:
                if cls.os.path.exists(cls.folder):
                    file = open(folder + "/" + cls.name + ".json", "w")
                else:
                    cls.os.mkdir(folder)
                    file = open(folder + "/" + cls.name + ".json", "w")
            file.write(saving)
            file.close()
        elif cls.data_type == "pickle":
            with open(cls.name + ".pickle", "wb") as file:
                cls.pickle.dump(cls.data, file)
        else:
            print("Invalid data type. Please use JSON or Pickle")
            
    @classmethod
    def get_new_data(cls,  name: str, data_type:str) -> object:
        
        cls.name = name
        cls.data_type = data_type
        
        flist = cls.os.listdir()
        full_fil_name = cls.name + "." +  cls.data_type
        if  full_fil_name  in flist:
        
            if cls.data_type == "json":
                json_data = open(cls.name + ".json", "r")
                json_read = json_data.read()
                mydata = cls.json.loads(json_read)
                json_data.close()
                return mydata
            elif cls.data_type == "pickle":
                with open(cls.name + ".pickle", "rb") as r:
                    mydata = cls.pickle.load(r)

                return mydata
            
        else:
            print("File name and/or extension is incorrect")
    
    @classmethod
    def get_current_data(cls) -> object:
        if cls.name == "default" and cls.folder == "." and cls.data == []:
            print("No current data saved in this instance")
            print("Please save data then try again")
            return None
        if cls.data_type == "json":
            if cls.folder == ".":
                json_data = open(cls.name + ".json", "r")
            else:
                json_data = open(cls.folder + "/" + cls.name + ".json", "r")
            json_read = json_data.read()
            mydata = cls.json.loads(json_read)
            json_data.close()
            return mydata
        elif cls.data_type == "pickle":
            with open(cls.name + ".pickle", "rb") as r:
                mydata = cls.pickle.load(r)
                
            return mydata

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    