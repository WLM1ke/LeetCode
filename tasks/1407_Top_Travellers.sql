# https://leetcode.com/problems/top-travellers/
SELECT U.name,
       IFNULL(SUM(R.distance), 0) AS travelled_distance
FROM Users AS U
         LEFT JOIN Rides AS R
                   ON U.id = R.user_id
GROUP BY U.id
ORDER BY travelled_distance DESC, U.name;