-- MS SQL Solution

select c.company_code,c.founder,
(select count(distinct lead_manager_code) from lead_manager lm where lm.company_code = c.company_code),
(select count(distinct senior_manager_code) from senior_manager sm where sm.company_code = c.company_code),
(select count(distinct manager_code) from manager m where m.company_code = c.company_code),
(select count(distinct employee_code) from employee e where e.company_code = c.company_code)
from company c
order by c.company_code