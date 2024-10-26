# mood_playlist_generator.py
import random

class PlaylistGenerator:
    def __init__(self):
        self.playlists = {
            "happy": {
                "working": ["Happy - Pharrell Williams", "Good Vibrations - The Beach Boys"],
                "exercising": ["Uptown Funk - Mark Ronson", "Can't Stop the Feeling! - Justin Timberlake"],
                "relaxing": ["Three Little Birds - Bob Marley", "Walking on Sunshine - Katrina and the Waves"]
            },
            "sad": {
                "working": ["Someone Like You - Adele", "The Night We Met - Lord Huron"],
                "exercising": ["Fix You - Coldplay", "Let Her Go - Passenger"],
                "relaxing": ["Stay - Rihanna", "The A Team - Ed Sheeran"]
            },
            "energetic": {
                "working": ["Titanium - David Guetta", "Stronger - Kanye West"],
                "exercising": ["Eye of the Tiger - Survivor", "Lose Yourself - Eminem"],
                "relaxing": ["Shake It Off - Taylor Swift", "Shut Up and Dance - WALK THE MOON"]
            },
            "relaxed": {
                "working": ["Weightless - Marconi Union", "Ocean Eyes - Billie Eilish"],
                "exercising": ["Breathe - Pink Floyd", "Come Away With Me - Norah Jones"],
                "relaxing": ["River Flows in You - Yiruma", "The Sound of Silence - Simon & Garfunkel"]
            }
        }

    def generate_playlist(self, mood, context):
        return self.playlists.get(mood, {}).get(context, ["No songs found for this mood and context."])
def get_user_input(prompt):
    return input(prompt).strip().lower()

def main():
    print("Welcome to the Mood-Based Music Playlist Generator!")

    while True:
        mood = get_user_input("Enter your current mood (happy, sad, energetic, relaxed): ")
        context = get_user_input("Enter your current context (working, exercising, relaxing): ")

        generator = PlaylistGenerator()
        playlist = generator.generate_playlist(mood, context)

        print("\n--- Your Playlist ---")
        for song in playlist:
            print(song)

        again = get_user_input("Would you like to generate another playlist? (yes/no): ")
        if again.lower() != 'yes':
            print("Thanks for using the Playlist Generator. Goodbye!")
            break
# mood_playlist_generator.py
import random

class PlaylistGenerator:
    def __init__(self):
        self.playlists = {
            "happy": {
                "working": ["Happy - Pharrell Williams", "Good Vibrations - The Beach Boys"],
                "exercising": ["Uptown Funk - Mark Ronson", "Can't Stop the Feeling! - Justin Timberlake"],
                "relaxing": ["Three Little Birds - Bob Marley", "Walking on Sunshine - Katrina and the Waves"]
            },
            "sad": {
                "working": ["Someone Like You - Adele", "The Night We Met - Lord Huron"],
                "exercising": ["Fix You - Coldplay", "Let Her Go - Passenger"],
                "relaxing": ["Stay - Rihanna", "The A Team - Ed Sheeran"]
            },
            "energetic": {
                "working": ["Titanium - David Guetta", "Stronger - Kanye West"],
                "exercising": ["Eye of the Tiger - Survivor", "Lose Yourself - Eminem"],
                "relaxing": ["Shake It Off - Taylor Swift", "Shut Up and Dance - WALK THE MOON"]
            },
            "relaxed": {
                "working": ["Weightless - Marconi Union", "Ocean Eyes - Billie Eilish"],
                "exercising": ["Breathe - Pink Floyd", "Come Away With Me - Norah Jones"],
                "relaxing": ["River Flows in You - Yiruma", "The Sound of Silence - Simon & Garfunkel"]
            }
        }

    def generate_playlist(self, mood, context):
        return self.playlists.get(mood, {}).get(context, ["No songs found for this mood and context."])

def get_user_input(prompt):
    return input(prompt).strip().lower()

def main():
    print("Welcome to the Mood-Based Music Playlist Generator!")

    while True:
        mood = get_user_input("Enter your current mood (happy, sad, energetic, relaxed): ")
        context = get_user_input("Enter your current context (working, exercising, relaxing): ")

        generator = PlaylistGenerator()
        playlist = generator.generate_playlist(mood, context)

        print("\n--- Your Playlist ---")
        for song in playlist:
            print(song)

        again = get_user_input("Would you like to generate another playlist? (yes/no): ")
        if again.lower() != 'yes':
            print("Thanks for using the Playlist Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
