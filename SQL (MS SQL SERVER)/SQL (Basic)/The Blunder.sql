select cast(ceiling(avg(cast(salary as float)) - avg(convert(float,replace(convert(varchar(50),salary),'0','')))) as int)
from employees