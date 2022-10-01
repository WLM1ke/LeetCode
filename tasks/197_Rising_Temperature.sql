-- https://leetcode.com/problems/rising-temperature/
SELECT C.id
FROM Weather AS C
         JOIN Weather AS P
              ON DATE_ADD(P.recordDate, INTERVAL 1 DAY)=C.recordDate
WHERE P.temperature < C.temperature;