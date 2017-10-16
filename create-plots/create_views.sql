drop view if exists term14;
drop view if exists term10;
drop view if exists term06;
drop view if exists term02;
drop view if exists term98;
drop view if exists term94;

create view term14 as
select * from anforande where dok_datum >= date('2014-10-15') and dok_datum < date('2018-10-15');

create view term10 as
select * from anforande where dok_datum >= date('2010-10-15') and dok_datum < date('2014-10-15');

create view term06 as
select * from anforande where dok_datum >= date('2006-10-15') and dok_datum < date('2010-10-15');

create view term02 as
select * from anforande where dok_datum >= date('2002-10-15') and dok_datum < date('2006-10-15');

create view term98 as
select * from anforande where dok_datum >= date('1998-10-15') and dok_datum < date('2002-10-15');

create view term94 as
select * from anforande where dok_datum >= date('1994-10-15') and dok_datum < date('1998-10-15');

