# sqlite3 < day02.sql
create table t(a int, b int);
.import --csv '|tr " ABCXYZ" ",123123" < day02.in' t
# Part 1
select sum(b+(4+b-a)%3*3) from t;
# Part 2
select sum((a+b)%3+1+(b-1)*3) from t;
