# https://leetcode.com/problems/exchange-seats/

WITH MAX_ID AS (SELECT MAX(ID) FROM Seat)
SELECT IF(id % 2 = 1 AND id not IN (select * from MAX_ID), id + 1,
          IF(id % 2 = 0, id - 1, id)) AS "id",
       student
FROM Seat
ORDER BY id;

