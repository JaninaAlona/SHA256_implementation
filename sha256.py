#https://qvault.io/cryptography/how-sha-2-works-step-by-step-sha-256/
from Preprocessor import Preprocessor
from MessageSchedule import MessageSchedule

password = "hello world"
password2 = "Append 44 bitsthee.435u453lkjhfdsh jhdfjhfdf"
password3 = "ate new kinds of financial applications. They can be decentralized, meaning that no single entity or person controls them and are nearly impossible to censor."

prepro = Preprocessor(password)
prepro.running()

msgSched = MessageSchedule(prepro.chunks)
msgSched.running()




#Hash value constants
H = [
    hex(0x6a09e667),
    hex(0xbb67ae85),
    hex(0x3c6ef372),
    hex(0xa54ff53a),
    hex(0x510e527f),
    hex(0x9b05688c),
    hex(0x1f83d9ab),
    hex(0x5be0cd19)
]

#Round constants
K = [
    hex(0x428a2f98), hex(0x71374491), hex(0xb5c0fbcf), hex(0xe9b5dba5), hex(0x3956c25b), hex(0x59f111f1), hex(0x923f82a4), hex(0xab1c5ed5),
    hex(0xd807aa98), hex(0x12835b01), hex(0x243185be), hex(0x550c7dc3), hex(0x72be5d74), hex(0x80deb1fe), hex(0x9bdc06a7), hex(0xc19bf174),
    hex(0xe49b69c1), hex(0xefbe4786), hex(0x0fc19dc6), hex(0x240ca1cc), hex(0x2de92c6f), hex(0x4a7484aa), hex(0x5cb0a9dc), hex(0x76f988da),
    hex(0x983e5152), hex(0xa831c66d), hex(0xb00327c8), hex(0xbf597fc7), hex(0xc6e00bf3), hex(0xd5a79147), hex(0x06ca6351), hex(0x14292967),
    hex(0x27b70a85), hex(0x2e1b2138), hex(0x4d2c6dfc), hex(0x53380d13), hex(0x650a7354), hex(0x766a0abb), hex(0x81c2c92e), hex(0x92722c85),
    hex(0xa2bfe8a1), hex(0xa81a664b), hex(0xc24b8b70), hex(0xc76c51a3), hex(0xd192e819), hex(0xd6990624), hex(0xf40e3585), hex(0x106aa070),
    hex(0x19a4c116), hex(0x1e376c08), hex(0x2748774c), hex(0x34b0bcb5), hex(0x391c0cb3), hex(0x4ed8aa4a), hex(0x5b9cca4f), hex(0x682e6ff3),
    hex(0x748f82ee), hex(0x78a5636f), hex(0x84c87814), hex(0x8cc70208), hex(0x90befffa), hex(0xa4506ceb), hex(0xbef9a3f7), hex(0xc67178f2)
]



