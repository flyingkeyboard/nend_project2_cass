import configparser


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP TABLES

staging_events_table_drop = "drop table IF EXISTS staging_events CASCADE"
staging_songs_table_drop = "drop table IF EXISTS staging_songs CASCADE"
songplay_table_drop = "drop table IF EXISTS songplays CASCADE"
user_table_drop = "drop table IF EXISTS users"
song_table_drop = "drop table IF EXISTS songs"
artist_table_drop = "drop table IF EXISTS artists"
time_table_drop = "drop table IF EXISTS time"

# CREATE TABLES

staging_events_table_create= ("""
""")

staging_songs_table_create = ("""
""")

songplay_table_create = ("create table songplays(songplay_id int,start_time text,"\
        + " user_id int not null,level text,song_id text,artist_id text,"\
        + " session_id int, location text, user_agent text, primary key(songplay_id))")

user_table_create = ("create table users(user_id int, first_name text not null,last_name text "\
            + "not null, gender char, level text not null, primary key(user_id))")

song_table_create = ("create table songs(song_id text, title text not null,"\
        + " artist_id text not null, year int not null, duration numeric"\
            + " not null, primary key(song_id))")

artist_table_create = ("create table artists(artist_id text, artist_name "\
                + " text, artist_location text, artist_latitude numeric,"\
                + " artist_longitude numeric,primary key(artist_id))")

time_table_create = ("create table time(start_time bigint,hour int not "\
            + " null, day int not null, week text not null, month text "\
            + " not null, year int not null, weekday text not null, primary key(start_time))")

# STAGING TABLES

staging_events_copy = ("""
""").format()

staging_songs_copy = ("""
""").format()

# FINAL TABLES

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS

create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
