-- MS SQL Solution

select co.continent, floor(avg(ci.population))
from city ci
inner join country co
    on co.code = ci.countrycode
group by co.continent