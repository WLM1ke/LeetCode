# https://leetcode.com/problems/department-highest-salary/

SELECT D.name   AS Department,
       E.name   AS Employee,
       E.salary AS Salary
FROM Employee AS E
         JOIN Department AS D
              ON E.departmentId = D.id
WHERE (E.salary, E.departmentId) IN (SELECT MAX(salary),
                                            departmentId
                                     FROM Employee
                                     GROUP BY departmentId);