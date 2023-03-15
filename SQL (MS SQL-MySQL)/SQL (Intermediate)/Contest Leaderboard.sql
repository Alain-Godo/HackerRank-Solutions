-- MS SQL Solution

with temp as(
select s.hacker_id hi, h.name n, max(s.score) maxscores
from Submissions s
inner join Hackers h
    on s.hacker_id = h.hacker_id
group by s.hacker_id, h.name, s.challenge_id
)
select t.hi, t.n, sum(maxscores) total
from temp t
group by t.hi, t.n
having sum(maxscores) > 0
order by total desc, t.hi