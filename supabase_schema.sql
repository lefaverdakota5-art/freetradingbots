-- Supabase schema for advanced trading app

create table if not exists users (
  id uuid primary key default gen_random_uuid(),
  email text unique,
  created_at timestamp default now()
);

create table if not exists bots (
  id uuid primary key default gen_random_uuid(),
  name text,
  owner uuid references users(id),
  created_at timestamp default now()
);

create table if not exists trades (
  id uuid primary key default gen_random_uuid(),
  bot_id uuid references bots(id),
  user_id uuid references users(id),
  symbol text,
  contract_type text,
  amount numeric,
  result text,
  created_at timestamp default now()
);

create table if not exists ai_votes (
  id uuid primary key default gen_random_uuid(),
  trade_id uuid references trades(id),
  model_name text,
  vote text,
  created_at timestamp default now()
);

create table if not exists transfers (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id),
  amount numeric,
  asset text,
  to_account text,
  status text,
  created_at timestamp default now()
);

create table if not exists balances (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references users(id),
  asset text,
  balance numeric,
  updated_at timestamp default now()
);
