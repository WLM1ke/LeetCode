# https://leetcode.com/problems/rank-scores/

SELECT S.score,
       (SELECT COUNT(DISTINCT score) FROM Scores WHERE score >= S.score) AS "rank"
FROM Scores AS S
ORDER BY S.score DESC;