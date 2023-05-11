class ArtistsSongs:

    def __init__(self, description: str) -> None:
        self.description = description
        self.artists_dict = {}
        self.songs_dict = {}

    def __str__(self):
        return f"{self.__class__}: {self.description}"

    def artists_reader(self, file_name: str):

        f = None
        try:
            f = open(file_name, 'r')
            for each_line in f.readlines():
                artist_id, artist_name = each_line.split(',')
                self.artists_dict[artist_id.strip()] = artist_name.strip()

        except IOError as e:
            print(e)

        finally:
            f.close()

        return self.artists_dict

    def songs_reader(self, file_name: str):
        f = None
        try:
            f = open(file_name, 'r')
            for each_line in f.readlines():
                song_order, song_id, song_name = each_line.split(',')
                self.songs_dict[song_name.strip()] = song_id.strip()

        except IOError as e:
            print(e)

        finally:
            f.close()

        return self.songs_dict


def main() -> None:

    a = ArtistsSongs("Lists a song for each artist")
    print(f"{a}")
    
    artists_dict = a.artists_reader("artists_songs/artists.txt")
    songs_dict = a.songs_reader("artists_songs/songs.txt")

    song_artist_list = []
    for song, id in songs_dict.items():
        if str(songs_dict[song]) in artists_dict:
            song_artist_list.append(
                f"{song}: {artists_dict[songs_dict[song]]}")

    for i, val in enumerate(sorted(song_artist_list)):
        print(f"{i} => {val}")


if __name__ == '__main__':
    main()
