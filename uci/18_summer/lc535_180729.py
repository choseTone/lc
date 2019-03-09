__author__ = 'wangqc'

'''
535. Encode and Decode TinyURL

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it 
returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm 
should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''

import random

class Codec:
    elements = [chr(c) for c in list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123))]

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.elements) for _ in range(6))
            if code not in self.code2url:
                self.url2code[longUrl], self.code2url[code] = code, longUrl
        return 'http://tinyurl.com/' + self.url2code[longUrl]

    def decode(self, shortUrl):
        return self.code2url[shortUrl[-6:]]


if __name__ == '__main__':
    from time import time

    codec = Codec()
    t = time()

    url = "https://leetcode.com/problems/design-tinyurl"
    encode = codec.encode(url)
    decode = codec.decode(encode)
    print('url: %s\nencode: %s\ndecode: %s\ntime: %.3fms' % (url, encode, decode, ((time() - t)) * 1000))
