drop table if exists urls;
drop table if exists users;
drop table if exists users_urls;
create table urls (
    id integer primary key autoincrement,
    `hash` text not null,
    `redirect_url` text not null
);
create table users (
    id integer primary key autoincrement,
    `username` text not null,
    `password` text not null,
    `email` text not null
);
create table users_urls (
    id integer primary key autoincrement,
    `user_id` integer not null,
    `url_id` integer not null
);
