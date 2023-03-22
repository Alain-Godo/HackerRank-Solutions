-- MS SQL Solution

select con.contest_id, con.hacker_id, con.name,
sum(total_submissions),
sum(total_accepted_submissions),
sum(total_views),
sum(total_unique_views)
from contests con
inner join colleges co
    on con.contest_id = co.contest_id
inner join challenges ch
    on ch.college_id = co. college_id
left join (select challenge_id, sum(total_views) total_views,
sum(total_unique_views) total_unique_views from view_stats group by challenge_id ) vs
    on vs.challenge_id = ch.challenge_id
left join (select challenge_id, sum(total_submissions) total_submissions,
sum(total_accepted_submissions) total_accepted_submissions from submission_stats group by challenge_id) ss
    on ss.challenge_id = ch.challenge_id
group by con.contest_id, con.hacker_id, con.name 
having (sum(total_submissions) != 0) or 
        (sum(total_accepted_submissions) != 0) or
        (sum(total_views) != 0) or
        (sum(total_unique_views) != 0)
order by con.contest_id 