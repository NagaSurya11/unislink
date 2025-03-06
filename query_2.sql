-- create cte with all attendance dates in single entry
with recursive attendance_single_dates as (
    select distinct name, start_date as date, end_date
    from unislink.attendance
    union all
    select a.name, date_add(a.date, interval 1 day) as date, a.end_date
    from attendance_single_dates a
    where date_add(a.date, interval 1 day) <= a.end_date
)

-- by month group and get the count of each individual
select name, month(date) as month, count(date) as total_days_in_month from attendance_single_dates
group by name, month
order by total_days_in_month desc
limit 1;