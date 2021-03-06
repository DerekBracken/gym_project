DROP TABLE bookings;
DROP TABLE sessions;
DROP TABLE members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    premium BOOLEAN
);

CREATE TABLE sessions (
    id  SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    time VARCHAR(255),
    day VARCHAR(255),
    capacity INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE
);

