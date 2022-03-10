-- import the database dump from htbn_0d_tvshows
SELECT tv_genres.name as 'name'
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id =  tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY name;
