import sqlite3

db = sqlite3.connect('spotify.db')

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS songs')

cursor.execute('CREATE TABLE IF NOT EXISTS songs(id INTEGER PRIMARY KEY, songName TEXT, artistName TEXT, genre TEXT, album TEXT, length TEXT)')

cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("The Black Hit Of Space", "The Human League", "Electronic", "Travelogue", "4.11")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Life Kills", "The Human League", "Electronic", "Travelogue", "3.07")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("WXJL Tonight", "The Human League", "Electronic", "Travelogue", "4.40")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Rock n Roll", "The Human League", "Electronic", "Travelogue", "3.17")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("The Things That Dreams Are Made Of", "The Human League", "Electronic", "Dare", "4.17")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("The Sound Of The Crowd", "The Human League", "Electronic", "Dare", "4.07")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Back Together", "Metronomy", "Alternative", "Summer 08", "3.41")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Miami Logic", "Metronomy", "Alternative", "Summer 08", "3.21")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Hang Me Out To Dry", "Metronomy", "Alternative", "Summer 08", "3.50")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("You Could Easily Have Me", "Metronomy", "Alternative", "Pip Paine (Pay The £5000 You Owe)", "3.07")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("How Say", "Metronomy", "Alternative", "Pip Paine (Pay The £5000 You Owe)", "4.29")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("In The D.O.D.", "Metronomy", "Alternative", "Pip Paine (Pay The £5000 You Owe)", "3.18")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Holiday", "Metronomy", "Alternative", "Nights Out", "4.14")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Back On The Motorway", "Metronomy", "Alternative", "Nights Out", "3.54")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Kids With Guns", "Gorillaz", "Indie Rock", "Demon Days", "3.45")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Feel Good Inc.", "Gorillaz", "Indie Rock", "Demon Days", "3.41")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Dare", "Gorillaz", "Indie Rock", "Demon Days", "4.04")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Ascension", "Gorillaz", "Indie Rock", "Humanz", "2.36")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("Interlude: The Non-Conformist Oath", "Gorillaz", "Indie Rock", "Humanz", "0.21")')
cursor.execute('INSERT INTO songs(songName, artistName, genre, album, length) VALUES ("The Apprentice", "Gorillaz", "Indie Rock", "Humanz", "3.54")')





db.commit()



cursor.execute('SELECT songName, artistName, genre, album, length FROM songs')

for row in cursor:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])


db.close()
