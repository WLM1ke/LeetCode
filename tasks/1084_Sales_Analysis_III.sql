# https://leetcode.com/problems/sales-analysis-iii/
SELECT P.product_id,
       P.product_name
FROM Product AS P
         JOIN Sales AS S
              USING (product_id)
GROUP BY S.product_id
HAVING SUM(S.sale_date >= "2019-01-01" AND S.sale_date < "2019-04-01") > 0
   AND SUM(S.sale_date < "2019-01-01" OR S.sale_date >= "2019-04-01") = 0;