-- MS SQL Solution

with temp as(
select w.id, wp.age, w.coins_needed, w.power
from wands w
inner join wands_property wp
    on w.code = wp.code
where (wp.is_evil = 0)
)
select t1.*
from temp t1
where t1.coins_needed = (select min(coins_needed) from temp t2 where (t1.age = t2.age) and (t1.power = t2.power))
order by t1.power desc, t1.age desc 