-- MS SQL Server

select sum(population)
from city
where countrycode in (select code from country where continent = 'Asia')