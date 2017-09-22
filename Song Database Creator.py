import sqlite3

db = sqlite3.connect('spotify.db')

cursor = db.cursor()

cursor.execute('DROP TABLE songs')

cursor.execute('CREATE TABLE IF NOT EXISTS songs(id INTEGER PRIMARY KEY, songName TEXT, artistName TEXT, genre TEXT, album TEXT, length REAL)')

cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("The Black Hit of Space", "The Human League", "Electronic", "Travelogue", 4.11)')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Life Kills", "The Human League", "Electronic", "Travelogue", 3.07)')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("WXJL Tonight", "The Human League", "Electronic", "Travelogue", 4.40)')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Rock n Roll", "The Human League", "Electronic", "Travelogue", 3.17)')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("The Things That Dreams Are Made Of", "The Human League", "Electronic", "Dare", 4.17)')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("The Sound Of The Crowd", "The Human League", "Electronic", "Dare", 4.07)')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Back Together", "Metronomy", "Alternative", "Summer 08", 3.41)')


db.commit()



cursor.execute('SELECT * FROM songs')

for row in cursor:
    print(row)
