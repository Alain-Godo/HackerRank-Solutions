-- MS SQL Solution

select distinct
case
    when f1.x <= f1.y then f1.x
    else f1.y
end x,
case
    when f1.x <= f1.y then f1.y
    else f1.x
end y
from (select *, row_number() over(order by x) num from Functions) f1
left join (select *, row_number() over(order by x) num from Functions) f2
    on (f1.x = f2.y) and (f1.y = f2.x) and (f1.num != f2.num)
where f2.x is not null
order by x