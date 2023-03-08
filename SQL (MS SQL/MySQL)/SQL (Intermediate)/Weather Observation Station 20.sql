-- MySQL Solution

with cte as (
    select s.*,
    row_number() over(order by lat_n) as position,
    count(*) over() as cnt
    from station s
)
select round(avg(lat_n),4)
from cte
where 
    (cnt%2 = 1 and position = (floor(cnt/2)) + 1) or
    (cnt%2 = 0 and position in (cnt/2,cnt/2 + 1))