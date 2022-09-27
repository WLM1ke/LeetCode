-- https://leetcode.com/problems/employees-earning-more-than-their-managers/
SELECT Employee.name AS Employee
FROM Employee
         JOIN Employee AS E
              ON Employee.managerId = E.id
WHERE Employee.salary > E.salary;