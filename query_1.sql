-- create cte 'without_duplicates'
with without_duplicates as (
    select distinct name, start_date, end_date from unislink.attendance
)
-- end - start + 1 will give the total days of attendance in entry
select name, sum(datediff(end_date, start_date) + 1) as total_days from without_duplicates
group by name
order by total_days desc
limit 1;
