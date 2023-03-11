-- MS SQL Solution

select c.*,
count(distinct e.lead_manager_code),
count(distinct e.senior_manager_code),
count(distinct e.manager_code),
count(distinct e.employee_code)
from company c
inner join employee e
    on c.company_code = e.company_code
group by c.company_code, c.founder
order by c.company_code

-- Alternative
--select c.*,
--count(distinct e.lead_manager_code),
--count(distinct e.senior_manager_code),
--count(distinct e.manager_code),
--count(distinct e.employee_code)
--from company c, employee e
--where c.company_code = e.company_code
--group by c.company_code, c.founder
--order by c.company_code