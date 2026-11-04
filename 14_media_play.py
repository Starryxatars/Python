class Media:
    def __init__(self, title):
        self.title = title

    def play(self):
        print(f"Playing media: {self.title}")


class Audio(Media):
    def play(self):
        print(f"Audio: Playing song '{self.title}' through speakers.")


class Video(Media):
    def play(self):
        print(f"Video: Playing '{self.title}' on screen with sound.")


class Podcast(Media):
    def __init__(self, title, host):
        super().__init__(title)
        self.host = host

    def play(self):
        print(f"Podcast: Playing episode '{self.title}' hosted by {self.host}.")


for m in (Audio("Kun Faya Kun"), Video("Interstellar"), Podcast("Tech Talk #12", "Riya")):
    m.play()
