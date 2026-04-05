from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

# -- MODEL FOR ARTIST --

class ArtistBase(SQLModel):
    name: str = Field(index=True)
    genre: Optional[str] = None

class Artist(ArtistBase, table= True):
    id: Optional[int] = Field(default= None, primary_key= True)

    albums: list["Album"] = Relationship(back_populates="artist")

class ArtistCreate(ArtistBase):
    pass

class ArtistPublic(ArtistBase):
    id: int

class ArtistUpdate(SQLModel):
    name: Optional[str] = None
    genre: Optional[str] = None

# -- MODEL FOR ALBUM --

class AlbumBase(SQLModel):
    title: str = Field(index= True)
    year: int
    artist_id: Optional[int] = Field(default= None, foreign_key= "artist.id")

class Album(AlbumBase, table= True):
    id: Optional[int] = Field(default= None, primary_key= True)
    artist: Optional[Artist] = Relationship(back_populates= "albums")

class AlbumCreate(AlbumBase):
    pass

class AlbumPublic(AlbumBase):
    id: int

class AlbumUpdate(SQLModel):
    title: Optional[str] = None
    year: Optional[int] = None
    artist_id: Optional[int] = None

#-- COMPOSITE MODELS --

class AlbumPublicWithArtist(AlbumBase):
    artist: Optional[ArtistPublic] = None

class ArtistPublicWithAlbums(ArtistPublic):
    albums: list[AlbumPublic] = []
