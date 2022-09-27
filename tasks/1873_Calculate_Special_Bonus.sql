-- https://leetcode.com/problems/calculate-special-bonus/

SELECT employee_id,
       (MOD(employee_id, 2) = 1 AND LEFT (name, 1) != "M") * salary AS bonus
FROM Employees
ORDER BY employee_id