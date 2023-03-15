-- MS SQL Solution

create table #temp (hi int, na varchar(50), cnt int)

insert into #temp
select h.hacker_id hi, h.name na, count(h.name) cnt
from Hackers h
inner join Challenges c
    on h.hacker_id = c.hacker_id
group by h.hacker_id, h.name;


with new_temp as(
select t.hi hi, t.na na, t.cnt cnt, max(t.cnt) over () maxi,
case
    when (select count(*) from #temp tt where tt.cnt = t.cnt) = 1 then 'U'
    else 'NU'
end is_unique
from #temp t
)
select nt.hi, nt.na, nt.cnt
from new_temp nt
where (nt.cnt = maxi) or (is_unique = 'U')
order by nt.cnt desc, nt.hi



