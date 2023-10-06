CREATE TABLE Movies (
    Name varchar(255) NOT NULL,
    Rating varchar(64) NOT NULL,
    Release_Year integer NOT NULL,
    Length varchar(64),
    Score real,
    Position smallint NOT NULL,
    Id uuid NOT NULL DEFAULT uuid_generate_v4(),
    CONSTRAINT movie_pkey PRIMARY KEY (Id)
);