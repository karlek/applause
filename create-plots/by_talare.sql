.load ./icu
.width 7 7 7 100

select
	round(1.0*applause/cnt, 4) as percentage,
	applause,
	cnt,
	talare,
	intressent_id
from (
	select count(*) as cnt, intressent_id, talare, sum(case when lower(anforandetext) like '%(applåder)%' then 1 else 0 end) as applause
	from anforande a1
	group by intressent_id
	having count(*) > 100
	order by cnt
)
order by percentage;
