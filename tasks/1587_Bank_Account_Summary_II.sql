# https://leetcode.com/problems/bank-account-summary-ii/
SELECT name,
       SUM(amount) AS balance
FROM Users
         JOIN Transactions
              USING (account)
GROUP BY account
HAVING SUM(amount) > 10000;