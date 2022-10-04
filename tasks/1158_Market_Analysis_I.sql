# https://leetcode.com/problems/market-analysis-i/
SELECT U.user_id                                AS buyer_id,
       U.join_date,
       SUM(IF(YEAR(O.order_date) = 2019, 1, 0)) AS orders_in_2019
FROM Users AS U
         LEFT JOIN Orders AS O
                   ON U.user_id = O.buyer_id
GROUP BY U.user_id;