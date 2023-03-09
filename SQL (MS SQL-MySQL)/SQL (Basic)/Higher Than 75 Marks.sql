-- MS SQL Solution

select name from students 
where marks > 75 order by substring(name,len(name)-2,3), id