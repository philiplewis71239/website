drop table if exists logs;
create table logs (
       id integer primary key autoincrement,
       ip_address text not null,
       timestamp text not null
);
