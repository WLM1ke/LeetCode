-- https://leetcode.com/problems/employees-with-missing-information/

SELECT Employees.employee_id
FROM Employees
         LEFT JOIN Salaries
                   ON Employees.employee_id = Salaries.employee_id
WHERE Salaries.employee_id IS NULL

UNION

SELECT Salaries.employee_id
FROM Employees
         RIGHT JOIN Salaries
                    ON Employees.employee_id = Salaries.employee_id
WHERE Employees.employee_id IS NULL

ORDER BY employee_id;