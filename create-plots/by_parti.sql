select
    parti,
    dok_datum,
    count(*) as count,
    sum(case when lower(anforandetext) like '%(applåder)%' then 1 else 0 end) applauded
from anforande as a1
where dok_datum >= date('2010-02-01') and ( 
    parti = 'c' or
    parti = 'kd' or
    parti = 'l' or
    parti = 'm' or
    parti = 'mp' or
    parti = 's' or
    parti = 'sd' or
    parti = 'v')
group by parti, dok_datum
order by dok_datum
;
