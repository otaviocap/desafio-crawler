CREATE TABLE Movies (
    Name varchar(255) NOT NULL,
    Rating varchar(64) NOT NULL,
    Release_Year integer NOT NULL,
    Length varchar(64),
    Score real,
    Position smallint NOT NULL,
    Id SERIAL not null,
    CONSTRAINT movie_pkey PRIMARY KEY (Id)
);