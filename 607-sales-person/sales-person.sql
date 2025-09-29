SELECT DISTINCT s.name
FROM SalesPerson s
LEFT JOIN Orders o ON s.sales_id = o.sales_id
LEFT JOIN Company c ON o.com_id = c.com_id
WHERE s.sales_id NOT IN (
    SELECT o2.sales_id
    FROM Orders o2
    JOIN Company c2 ON o2.com_id = c2.com_id
    WHERE c2.name = 'RED'
);
