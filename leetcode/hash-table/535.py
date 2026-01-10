class Codec:

    def __init__(self):
        self.url_map = dict()

    def get_uuid(self, length=8):

        uuid = ""

        base = ""
        base += "abcdefghjiklmnopqrstuvtxyz"
        base += "abcdefghjiklmnopqrstuvtxyz".upper()
        base += "1234567890"

        for _ in range(length):
            uuid += random.choice(base)

        return uuid

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        uuid = self.get_uuid()
        self.url_map[uuid] = longUrl
        return f"http://tinyurl.com/{uuid}"

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        uuid = shortUrl.split("/")[-1]
        return self.url_map[uuid]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
