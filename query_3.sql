-- create cte with all attendance dates in single entry
with recursive attendance_single_dates as (
    select distinct name, start_date as date, end_date
    from unislink.attendance
    union all
    select a.name, date_add(a.date, interval 1 day) as date, a.end_date
    from attendance_single_dates a
    where date_add(a.date, interval 1 day) <= a.end_date
),
-- create cte of consecutive days where group is starting date of consecutive date
consecutivedates as (
    select name, date, date_sub(date, INTERVAL ROW_NUMBER() over (PARTITION BY name ORDER by date) DAY) AS grp
    from attendance_single_dates
)

-- all the consecutive days has its starting date as grp apply group and count of total
select name, count(*) as consecutive_days from consecutivedates
group by name, grp
order by consecutive_days desc
limit 1;