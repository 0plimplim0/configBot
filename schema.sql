create table if not exists settings(
    guild_id integer,
    key text,
    value text,
    primary key (guild_id, key)
);