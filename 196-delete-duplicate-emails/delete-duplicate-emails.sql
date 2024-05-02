# Write your MySQL query statement below
DELETE from Person where Id not in
(select id from (select min(id) as id from Person group by email ) as p)