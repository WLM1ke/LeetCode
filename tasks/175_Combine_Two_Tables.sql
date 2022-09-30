-- https://leetcode.com/problems/combine-two-tables/
SELECT firstName,
       lastName,
       city,
       state
FROM Person
         LEFT JOIN Address
                   USING (personId);