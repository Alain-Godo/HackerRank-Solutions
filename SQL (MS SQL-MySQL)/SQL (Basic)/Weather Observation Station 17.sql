-- MySQL Solution

select round(s1.long_w,4)
from station s1
where s1.lat_n = (select min(s2.lat_n) from station s2 where s2.lat_n > 38.7780)