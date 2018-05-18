import sqlite3
import os
from passlib.apps import custom_app_context as pwd_context
from faker import Faker

schema = """
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
"""

add_user_query = """
    insert into `users` (username, password, email) values (?, ?, ?)
"""

add_test_url_query = """
    insert into `urls` (hash, redirect_url) values (?, ?)
"""

conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'shawty.db'))

cursor = conn.cursor()

cursor.executescript(schema)
cursor.execute(add_user_query, ["bob", pwd_context.hash("bobsupersecret"), "bob@bobsbobbins.com"])
for _ in range(5):
    some_fake = Faker()
    opts = [some_fake.user_name(), some_fake.password(), some_fake.email()]
    cursor.execute(add_user_query, opts)
    
cursor.execute(add_test_url_query, ['some_other_hash', 'https://google.com'])

conn.commit()
cursor.close()
conn.close()
