# ImportError: No module named 'Crypto' 오류로 인한 import 
import sys
import crypto
sys.modules['Crypto'] = crypto

from Crypto.Cipher import AES

# Key는 암호화나 MAC 계산에 쓰이는 데이터를 의미한다.
key = bytes([
    0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 
    0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF
    ])

# AAD는 추가 인증 데이터를 의미한다.
aad = bytes([
    0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
    0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E
    ])

# Nonce는 Key나 AAD에 할당되는 유일한 값을 의미한다.
nonce = bytes(
    [0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB]
) 

# 원본 데이터
plain_data = bytes([0x41, 0x42, 0x43, 0x45, 0x47, 0x48,
                    0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E])

# 암호화 라이브러리 생성
cipher = AES.new(key, AES.MODE_CCM, nonce)

# AAD 추가
cipher.update(aad)

# 암호화
cipher_data = cipher.encrypt(plain_data)
mac = cipher.digest()


her
# 복호화 라이브러리 생성 및 AAD 추가
cipher = AES.new(key, AES.MODE_CCM, nonce)
cipher.update(aad)

# 복호화 데이터
decrpyt_data = cipher.decrypt_and_verify(cipher_data, mac)
print("cipher_data =", cipher_data)
print("mac =", mac)
print("decrpyt_data =", decrpyt_data)
