import rsa

key = rsa.newkeys(3000)		#產生隨機金鑰
privateKey = key[1]			#私密金鑰
publicKey = key[0]			#公開金鑰

message = '中國山東煙臺.Now is better than never.'
print('Before encrypted:',message)
message = message.encode()

cryptedMessage = rsa.encrypt(message, publicKey)
print('After encrypted:\n',cryptedMessage)

message = rsa.decrypt(cryptedMessage, privateKey)
message = message.decode()
print('After decrypted:',message)
