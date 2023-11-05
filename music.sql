CREATE TABLE artists (
    id INTEGER PRIMARY KEY,
    artist_name TEXT);


CREATE TABLE albums (
	id INTEGER PRIMARY KEY,
	album_title TEXT,
	artist_name TEXT);


CREATE TABLE songs (
	id INTEGER PRIMARY KEY,
	song_title TEXT,
	album_title TEXT,
	track_no INTEGER,
	length INTEGER);
