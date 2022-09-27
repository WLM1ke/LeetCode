-- https://leetcode.com/problems/delete-duplicate-emails/
DELETE
Person
FROM Person JOIN Person AS P2
WHERE
    Person.email = P2.email
    AND
    Person.id > P2.id