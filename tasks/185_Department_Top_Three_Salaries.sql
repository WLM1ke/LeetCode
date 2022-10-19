# https://leetcode.com/problems/department-top-three-salaries/

SELECT D.name   AS 'Department',
       E.name   AS 'Employee',
       E.salary AS 'Salary'
FROM Employee AS E
         JOIN Department AS D
              ON E.departmentId = D.id
WHERE (SELECT COUNT(DISTINCT salary)
       FROM Employee
       WHERE salary >= E.salary
         AND departmentId = E.departmentId) <= 3;