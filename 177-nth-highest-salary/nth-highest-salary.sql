CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
   select salary from (select salary, row_number() over(order by salary desc) as rn from employee group by salary) as temp where rn = N
  );
END