# https://leetcode.com/problems/trips-and-users/
SELECT T.request_at                                    AS "Day",
       ROUND(AVG(IF(T.status = "completed", 0, 1)), 2) AS "Cancellation Rate"
FROM Trips AS T
         JOIN Users AS D
              ON T.driver_id = D.users_id
         JOIN Users AS C
              ON T.client_id = C.users_id
WHERE D.banned = "No"
  AND C.banned = "No"
  AND T.request_at BETWEEN "2013-10-01" AND "2013-10-03"
GROUP BY T.request_at
ORDER BY T.request_at;