# Write your MySQL query statement below
SELECT e1.email
FROM Person e1
JOIN Person e2 ON e2.email = e1.email
WHERE e1.id > e2.id;