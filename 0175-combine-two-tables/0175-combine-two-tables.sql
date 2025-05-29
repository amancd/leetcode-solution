# Write your MySQL query statement below
SELECT p.firstName, p.lastName, q.city, q.state
FROM Person p
LEFT JOIN Address q ON p.personId = q.personId