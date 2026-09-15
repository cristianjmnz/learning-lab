CREATE DATABASE IF NOT EXISTS videogames_db;
USE videogames_db;

CREATE TABLE videogames (
    id INT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    developer VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    playtime_hours INT NOT NULL
);

INSERT INTO videogames (id, title, developer, year, playtime_hours) VALUES
(1, 'The Legend of Zelda', 'Nintendo', 1986, 20),
(2, 'Super Mario Bros.', 'Nintendo', 1985, 10),
(3, 'Final Fantasy VII', 'Square Enix', 1997, 40),
(4, 'The Witcher 3', 'CD Projekt Red', 2015, 100),
(5, 'Minecraft', 'Mojang Studios', 2011, 9999),
(6, 'Grand Theft Auto V', 'Rockstar Games', 2013, 80),
(7, 'Dark Souls', 'FromSoftware', 2011, 60),
(8, 'Portal 2', 'Valve', 2011, 8),
(9, 'Red Dead Redemption 2', 'Rockstar Games', 2018, 70),
(10, 'The Last of Us', 'Naughty Dog', 2013, 15),
(11, 'Halo: Combat Evolved', 'Bungie', 2001, 10),
(12, 'God of War', 'Santa Monica Studio', 2018, 25);