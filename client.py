import requests

artists_url = "http://127.0.0.1:8000/artists"
albums_url = "http://127.0.0.1:8000/albums"
root_url = "http://127.0.0.1:8000/"

def read_root():
    print(" --- ROOT ---")
    data = requests.get(root_url)
    print(f"Status: {data.status_code}")
    print(f"Response: {data.json()}")

# -- ENDPOINTS OF THE ARTISTS

def read_artists():
    print(" --- READ ALL ARTISTS --- ")
    data = requests.get(f"{artists_url}/")
    print(f"Status: {data.status_code}")
    for artist in data.json():
        print(artist)

def read_artist(artist_id: int):
    print(f"--- READ ARTIST BY ID: {artist_id}")
    data = requests.get(f"{artists_url}/{artist_id}")
    print(f"Status: {data.status_code}")
    print(data.json())

def create_artist():
    print("--- CREATE ARTIST ---")
    new_artist = {"name": "The Weeknd", "genre": "R&B"}

    data = requests.post(f"{artists_url}/", json=new_artist)
    print(f"Status: {data.status_code}")
    print(data.json())
    return data.json()["id"] if data.status_code == 200 else None

def update_artist(artist_id: int):
    print("--- UPDATE ARTIST ---")
    update_data = {"genre": "Pop Soul"}
    data = requests.patch(f"{artists_url}/{artist_id}", json=update_data)
    print(f"Status: {data.status_code}")
    print(data.json())

def delete_artist(artist_id: int):
    print("--- DELETE ARTIST ---")
    data = requests.delete(f"{artists_url}/{artist_id}")
    print(f"Status: {data.status_code}")
    print(data.json())

# -- ENDPOINTS OF THE ALBUMS --

def read_albums():
    print("--- READ ALL ALBUMS")
    data = requests.get(f"{albums_url}/")
    print(f"Status: {data.status_code}")
    print(data.json())

def read_album(album_id: int):
    print("--- READ ALBUM BY ID ---")
    data = requests.get(f"{albums_url}/{album_id}")
    print(f"Status: {data.status_code}")
    print(data.json())

def create_album(artist_id: int):
    print("--- CREATE ALBUM ---")
    new_album = {"title": "After Hours", "year": 2020, "artist_id":artist_id}
    data = requests.post(f"{albums_url}/", json=new_album)
    print(f"Status: {data.status_code}")
    print(data.json())
    return data.json()["id"] if data.status_code == 200 else None

def delete_album(album_id: int):
    print("--- DELETE ALBUM ---")
    data = requests.delete(f"{albums_url}/{album_id}")
    print(f"Status: {data.status_code}")
    print(data.json())

def read_artists_and_albums(artist_id: int):
    print("--- READ ARTISTS AND ALBUMS ---")
    data = requests.get(f"{artists_url}/{artist_id}")
    print(f"Status: {data.status_code}")

    for key, value in data.json().items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    read_root()

    read_artists()
    read_albums()

    new_id_artist = create_artist()

    if new_id_artist:
        read_artist(new_id_artist)

        update_artist(new_id_artist)

        new_id_album = create_album(new_id_artist)

        if new_id_album:
            read_album(new_id_album)

            read_artists_and_albums(new_id_artist)

            delete_album(new_id_album)

        read_albums()

        delete_artist(new_id_artist)
