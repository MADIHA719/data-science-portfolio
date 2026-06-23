-- BS Data Science Portfolio: Project 05
-- Title: Retail Analytics & Database Query Case Study
-- Description: Demonstrates relational database design and business analytics using SQL.
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;
-----------------------------------------------------------
-- 1. DATABASE SCHEMA
-----------------------------------------------------------

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    Country VARCHAR(50)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-----------------------------------------------------------
-- 2. DATA INSERTION
-----------------------------------------------------------

INSERT INTO Customers VALUES
(1, 'Alice Smith', 'USA'),
(2, 'Bob Jones', 'UK'),
(3, 'Charlie Brown', 'USA'),
(4, 'Diana Prince', 'Canada');

INSERT INTO Orders VALUES
(101, 1, '2026-06-01', 250.00),
(102, 2, '2026-06-02', 80.00),
(103, 1, '2026-06-05', 150.00),
(104, 3, '2026-06-10', 450.00),
(105, 4, '2026-06-12', 300.00);

-----------------------------------------------------------
-- 3. BUSINESS ANALYTICS QUERIES
-----------------------------------------------------------

-- A: Order Details (JOIN)
SELECT 
    o.OrderID,
    c.CustomerName,
    o.OrderDate,
    o.TotalAmount
FROM Orders o
INNER JOIN Customers c
ON o.CustomerID = c.CustomerID;

-- B: Customer Lifetime Value (LTV)
SELECT 
    c.CustomerName,
    COUNT(o.OrderID) AS Total_Orders,
    COALESCE(SUM(o.TotalAmount), 0) AS Lifetime_Spend
FROM Customers c
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName
ORDER BY Lifetime_Spend DESC;

-- C: Country Performance Analysis
SELECT 
    c.Country,
    COUNT(o.OrderID) AS Transactions,
    AVG(o.TotalAmount) AS Avg_Order_Value
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.Country
HAVING AVG(o.TotalAmount) >= 150;
