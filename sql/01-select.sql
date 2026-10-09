USE videogames_db;

SELECT * FROM videogames;

#Muestra solo los desarrolladores que tienen más de 1 videojuego. 
#Muestra developer y el total (alias 'total').
SELECT developer, COUNT(*) AS total 
FROM videogames 
GROUP BY developer 
HAVING COUNT(*) > 1;