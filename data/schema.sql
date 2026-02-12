create table if not exists settings(
    guild_id integer,
    key text,
    value text,
    primary key (guild_id, key)
);

create table if not exists role_permissions(
    guild_id integer,
    role_id integer,
    command text,
    allowed integer
)