from typing import List
from fastapi import FastAPI, HTTPException, Query, Depends
from sqlmodel import Session, select

from models import *

from database import lifespan, get_session

app= FastAPI(lifespan=lifespan)

# -- HOME ROOT --
@app.get("/")
def read_root():
    return {
        "message" : "Welcome to the Music API (Artist and Albums)",
        "Description" : "This API allows you to perform CRUD operations on artist and their albums"
    }

# -- END POINTS OF THE ALBUMS --

@app.get("/albums/", response_model=List[AlbumPublic])
def read_albums(offset: int = 0, limit: int = Query(default= 100, le= 100), session: Session = Depends(get_session)):
    albums = session.exec(select(Album).offset(offset).limit(limit)).all()
    return albums

@app.get("/albums/{album_id}", response_model= AlbumPublicWithArtist)
def read_album(album_id: int, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    return album

@app.post("/albums/", response_model=AlbumPublic)
def create_album(album: AlbumCreate, session: Session = Depends(get_session)):
    db_album =Album.model_validate(album)
    session.add(db_album)
    session.commit()
    session.refresh(db_album)
    return db_album

@app.patch("/albums/{album_id}", response_model=AlbumPublic)
def update_album(album_id: int, album: AlbumUpdate, session: Session = Depends(get_session)):
    db_album = session.get(Album, album_id)
    if not db_album:
        raise HTTPException(status_code=404, detail="Album not found")
    album_data = album.model_dump(exclude_unset= True)
    for key, value in album_data.items():
        setattr(db_album, key, value)

    session.add(db_album)
    session.commit()
    session.refresh(db_album)
    return db_album

@app.delete("/albums/{album_id}")
def delete_album (album_id: int, session: Session = Depends(get_session)):
    album = session.get(Album, album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    session.delete(album)
    session.commit()
    return {"ok": True}

# -- END POINTS OF THE ARTIST --

@app.get("/artists/", response_model=list[ArtistPublic])
def read_artists(offset: int = 0, limit: int = Query(default=100, le=100), session: Session = Depends(get_session)):
    artists = session.exec(select(Artist).offset(offset).limit(limit)).all()
    return artists

@app.get("/artists/{artist_id}", response_model=ArtistPublicWithAlbums)
def read_artist(artist_id: int, session: Session = Depends(get_session)):
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@app.post("/artists/", response_model=ArtistPublic)
def create_artist(artist: ArtistCreate, session: Session = Depends(get_session)):
    db_artist = Artist.model_validate(artist)
    session.add(db_artist)
    session.commit()
    session.refresh(db_artist)
    return db_artist

@app.patch("/artists/{artist_id}", response_model=ArtistPublic)
def update_artist(artist_id: int, artist: ArtistUpdate, session: Session = Depends(get_session)):
    db_artist = session.get(Artist, artist_id)
    if not db_artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    artist_data = artist.model_dump(exclude_unset=True)
    for key, value in artist_data.items():
        setattr(db_artist, key, value)

    session.add(db_artist)
    session.commit()
    session.refresh(db_artist)
    return db_artist

@app.delete("/artists/{artist_id}")
def delete_artist(artist_id: int, session: Session = Depends(get_session)):
    artist = session.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    session.delete(artist)
    session.commit()
    return {"ok": True}