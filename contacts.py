
import json,os

class phonebook:

    def __init__(self,filename='c.json'):

        if os.path.isfile(filename):

            self.file = open(filename,'r+')
            self.file_data = json.load(self.file)

    def display(self):

        x = [print(i,'\n') for i in self.file_data['contacts']]
        return f"{x}"

    def add(self,data,filename='c.json'):

        with open(filename, 'r+') as file:
            self.file_data = json.load(file)
            self.file_data['contacts'].append(data)
            file.seek(0)
            json.dump(self.file_data, file,indent=4)

    def search(self,name):

        for person in self.file_data['contacts']:
            if person['name'] == name:
                print(f"Name:{person['name']} Phone: {person['phone']} Email:{person['email']}")
    
    def delete(self, name):

        for person in range(len(self.file_data['contacts'])):
            if (self.file_data[person]['name']==name):
                del self.file_data[person]
                break
    
    def menu(self):
        print("Choice operations:\n1.Add contacts.\n2.Display all contacts.\n3.Search contacts.\n4.delete "
              "contacts.\n6.Quit from contacts. ")
