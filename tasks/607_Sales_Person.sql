# https://leetcode.com/problems/sales-person/
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT O.sales_id
    FROM Orders AS O
             JOIN Company AS C
                  USING(com_id)
    WHERE C.name="RED"
);