
from abc import ABC ,abstractmethod
class Person (ABC):
    def __init__(self,name:str, employee_id:str):
        self.name =name
        self.employee_id =employee_id

    @abstractmethod
    def get_role(self)->str:
       pass


class Employee(Person):
    def __init__(self, name:str, employee_id:str,role:str):
        super().__init__(name, employee_id)
        self.role =role

    def get_role(self)->str:
        return self.role
    
    def __str__(self)->str:
        return f"Employee:{self.name} (ID:{self.employee_id},Role:{self.role})"


employee =Employee("Gashaw Gedef","Cust001","Administrator")


print(employee)
