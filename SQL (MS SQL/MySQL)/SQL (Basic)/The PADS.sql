-- MS SQL Solution

select concat(name,'(',substring(occupation,1,1),')') as c 
from occupations 

UNION

select CONCAT('There are a total of ',count(occupation),' ',lower(occupation),'s.')  
from occupations
group by occupation
order by c