select  name , EmployeeUNI.unique_id as unique_id from EmployeeUNI
right join Employees
on EmployeeUNI.id = Employees.id

