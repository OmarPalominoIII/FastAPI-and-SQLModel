from sqlmodel import Session
from models import Artist, Album
from database import engine, create_db_and_tables

def create_samples():

    with Session(engine) as session:
        # -- Create Artist --
        daft_punk = Artist(name="Daft Punk", genre="Electronic")
        rosalia = Artist(name="Rosalia", genre="Flamenco pop")
        bad_bunny = Artist(name="Bad bunny", genre= "Reggaeton")
        romeo_santos = Artist(name="Romeo Santos", genre="Bachata")
        metallica = Artist(name="Metallica", genre="Rock")
        the_neighbourhood = Artist(name="The Neighbourhood", genre= "Indie Pop")

        session.add(daft_punk)
        session.add(rosalia)
        session.add(bad_bunny)
        session.add(romeo_santos)
        session.add(metallica)
        session.add(the_neighbourhood)
        session.commit()

        session.refresh(daft_punk)
        session.refresh(rosalia)
        session.refresh(bad_bunny)
        session.refresh(romeo_santos)
        session.refresh(metallica)
        session.refresh(the_neighbourhood)

        print("Created artist: ", daft_punk)
        print("Created artist: ", rosalia)
        print("Created artist: ", bad_bunny)
        print("Created artist: ", romeo_santos)
        print("Created artist: ", metallica)
        print("Created artist: ", the_neighbourhood)

        # -- Create Albums --
        discovery = Album(title="Discovery", year=2001, artist_id=daft_punk.id)
        motomami = Album(title="Motomami", year=2022, artist_id=rosalia.id)
        oasis = Album(title="Oasis", year=2019, artist_id=bad_bunny.id)
        formula = Album(title="Formula", year=2011, artist_id=romeo_santos.id)
        master_of_puppets = Album(title="Master of puppets", year=1986, artist_id=metallica.id)

        # -- Album without artist
        im_sorry = Album(title="I'm sorry", year=2012)

        session.add(discovery)
        session.add(motomami)
        session.add(oasis)
        session.add(formula)
        session.add(master_of_puppets)
        session.add(im_sorry)
        session.commit()

        session.refresh(discovery)
        session.refresh(motomami)
        session.refresh(oasis)
        session.refresh(formula)
        session.refresh(master_of_puppets)
        session.refresh(im_sorry)

        print("Create album: ", discovery.title, " by: ", daft_punk.name)
        print("Create album: ", motomami.title, " by: ", rosalia.name)
        print("Create album: ", oasis.title, " by: ", bad_bunny.name)
        print("Create album: ", formula.title, " by: ", romeo_santos.name)
        print("Create album: ", master_of_puppets.title, " by: ", metallica.name)

        # -- Update album --
        im_sorry.artist = the_neighbourhood
        session.add(im_sorry)
        session.commit()
        session.refresh(im_sorry)
        print("Updated album: ", im_sorry.title, " by: ", the_neighbourhood.name)

        # -- Create albums and add artist
        x100pre = Album(title="X100PRE", year= 2018)
        eutdm = Album(title="El ultimo tour del mundo", year= 2020)

        bad_bunny.albums.append(x100pre)
        bad_bunny.albums.append(eutdm)

        session.add(bad_bunny)
        session.commit()

        print(f"Artist {bad_bunny.name} updated with {len(bad_bunny.albums)} albums in total")

def main():
    create_db_and_tables()
    create_samples()

if __name__ == "__main__":
    main()





