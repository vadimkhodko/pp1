class Song():
    
    def __init__(self,performer,song,album,year):
        self.performer = performer
        self.song = song
        self.album = album
        self.year = year
    
    def __str__(self):
        return f"performer: {self.performer}\n song: {self.song}\n album: {self.album}\n year: {self.album}"
    
song1 = Song("Ed Sheeran", "Hearts Dont Break Around Here" "Divide", "2017")
print(song1)      
