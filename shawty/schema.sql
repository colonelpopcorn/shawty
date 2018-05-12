drop table if exists urls;
create table urls (
    id integer primary key autoincrement,
    `hash` text not null
    `redirect_url` text not null
)