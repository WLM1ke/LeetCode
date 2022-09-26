-- https://leetcode.com/problems/find-customer-referee

SELECT name
FROM (SELECT *
      FROM Customer
      WHERE referee_id != 2 OR referee_id is NULL)
         AS T