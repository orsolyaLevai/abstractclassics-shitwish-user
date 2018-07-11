create table if not exists shitwishusers
(
  id           serial       not null,
  first_name   varchar(255) not null,
  last_name    varchar(255) not null,
  email        varchar(255) not null,
  password     varchar(255) not null,
  address      varchar(255) not null,
  phone_number varchar(255) not null,
  constraint shitwishusers_pkey
  primary key (id)
);

create unique index if not exists shitwishusers_email_uindex
  on shitwishusers (email);