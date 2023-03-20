-- MS SQL Server

select ci.name
from city ci
inner join country co
    on co.code = ci.countrycode
where co.continent = 'Africa'