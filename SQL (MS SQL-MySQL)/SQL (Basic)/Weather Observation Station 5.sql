-- MS SQL Solution

select * from (select top 1 city, LEN(city) cityLength from station order by cityLength ASC,city ASC) Minimum
UNION ALL
select * from (select top 1 city, LEN(city) cityLength from station order by cityLength desc, city ASC) Maximum