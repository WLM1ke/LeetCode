# https://leetcode.com/problems/human-traffic-of-stadium/

WITH T AS (SELECT id,
                  visit_date,
                  people
           FROM Stadium
           WHERE people >= 100)

SELECT DISTINCT *
FROM T
WHERE id IN (SELECT id FROM T) AND id + 1 IN (SELECT id FROM T) AND id + 2 IN (SELECT id FROM T)
   OR id IN (SELECT id FROM T) AND id + 1 IN (SELECT id FROM T) AND id - 1 IN (SELECT id FROM T)
   OR id IN (SELECT id FROM T) AND id - 1 IN (SELECT id FROM T) AND id - 2 IN (SELECT id FROM T)
ORDER BY id;
