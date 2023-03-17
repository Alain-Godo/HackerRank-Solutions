-- MS SQL Solution

select s.name
from Friends f
inner join Students s
    on f.id = s.id
inner join Packages p
    on f.id = p.id 
inner join Packages p2  
    on f.friend_id = p2.id
where p.salary < p2.salary
order by p2.salary
