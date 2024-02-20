from lyricsgenius import Genius
import os
import csv
import re

# Donde se guardarán los coros
csv_filename = 'datasets/choruses.csv'

# Conjunto para almacenar canciones ya procesadas
processed_songs = set()

def __save(chorus: str, artist_name: str, song_title: str):
    # Reemplazar los saltos de línea con espacios para el coro
    chorus_no_newlines = chorus.replace('\n', ' ')

    # Verificar si el coro no es una cadena vacía
    if not chorus_no_newlines.strip():
        print(f"No se encontró el coro para la canción '{song_title}' de {artist_name}.")
        return

    # Verificar si el archivo CSV ya existe
    file_exists = os.path.isfile(csv_filename)
    
    # Escribir en el archivo CSV
    with open(csv_filename, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Escribir la cabecera si el archivo es nuevo
            writer.writerow(['Artist', 'Song Title', 'Chorus'])
        # Escribir el coro en una nueva fila
        writer.writerow([artist_name, song_title, chorus_no_newlines])

def __download_chorus(artist_name: str, song_title: str) -> str:
    search_query = f"{artist_name} {song_title}"
    song = genius.search_song(search_query)

    if song is None:
        print(f"No se encontró la canción '{song_title}' de {artist_name}.")
        return ''

    lyrics = song.lyrics

    chorus_pattern = r'\[Chorus\](.*?)(?=\[|\Z)'
    match = re.search(chorus_pattern, lyrics, re.DOTALL)
    if match:
        chorus_lyrics = match.group(1).strip()
    else:
        chorus_lyrics = ''

    return chorus_lyrics

def download_choruses(artists: list):
    for artist_name in artists:
        try:
            # Buscar todas las canciones del artista
            artist = genius.search_artist(artist_name, max_songs=3, sort='popularity')
            songs = artist.songs

            # Extraer el coro de cada canción
            for song in songs:
                # Extraer el título de la canción del objeto de canción
                song_title = song.title

                # ... (resto del código existente para procesar cada canción)

                # Intenta descargar el coro y guardarlos
                chorus = __download_chorus(artist_name, song_title)
                if chorus.strip():  # Verifica que el coro no esté vacío
                    __save(chorus, artist_name, song_title)

        except TimeoutError:
            print(f"Se ha producido un error de tiempo de espera al intentar descargar el coro de {artist_name}.")
        except Exception as e:
            print(f"Se ha producido un error al intentar descargar el coro de {artist_name}: {e}")
            continue  # Continúa con el siguiente artista o canción