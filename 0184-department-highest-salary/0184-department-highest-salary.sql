# Write your MySQL query statement below
SELECT Department.name As Department, Employee.name As Employee, salary AS Salary
FROM Employee 
LEFT JOIN Department ON Employee.departmentId = Department.id
WHERE (Employee.departmentId, Employee.salary) IN (
    SELECT departmentID, MAX(salary)
    FROM Employee
    GROUP BY departmentId
)