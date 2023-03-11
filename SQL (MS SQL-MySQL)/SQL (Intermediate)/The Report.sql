-- MS SQL Solution

select case when g.grade >= 8 then s.name else NULL end n,
g.grade, s.marks
from students s
inner join grades g
    on (s.marks > g.min_mark) and (s.marks < g.max_mark)
order by g.grade desc, n , s.marks

-- Alternative

-- with studentswithgrade as(
--     select s.name name , s.marks marks,
--     (select grade from grades where (s.marks >= min_mark) and (s.marks <= max_mark)) grade
--     from students s
-- )
-- select case when s.grade>=8 then s.name else NULL end n,
-- s.grade, s.marks
-- from studentswithgrade s
-- order by s.grade desc, n , s.marks
