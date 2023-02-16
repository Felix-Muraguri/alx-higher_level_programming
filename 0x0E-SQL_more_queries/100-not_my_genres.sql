-- list all genres not linked to the show Better Call Saul
SELECT tv_genres.name AS name
FROM tv_sgenres
     JOIN tv_genres.id = tv_show_genres_id
JOIN tv_shows
	     ON tv_show_genres.show_id = tv_shows.id
		WHERE tv_shows.title = "Better Call Saul"
			ORDER BY tv_genres.id
		) better_call_saul_genres ON better_call_saul_genres.id = tv_genres.id
		WHERE better_call_saul_genres.id is NULL
		ORDER BY name;


