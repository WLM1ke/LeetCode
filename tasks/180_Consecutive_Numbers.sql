# https://leetcode.com/problems/consecutive-numbers/
SELECT DISTINCT Logs.Num AS ConsecutiveNums
FROM Logs
         JOIN Logs AS Lag1
              ON Lag1.id = Logs.id - 1
         JOIN Logs AS Lag2
              ON Lag2.id = Logs.id - 2
WHERE Logs.Num = Lag1.Num
  AND Logs.Num = Lag2.Num;