# Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM product p INNER JOIN sales s
ON s.product_id = p.product_id