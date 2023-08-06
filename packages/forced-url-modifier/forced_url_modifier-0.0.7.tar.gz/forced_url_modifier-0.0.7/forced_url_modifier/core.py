# use foced_url_decoding & forced_url_encoding
class URL_Modifier:
    
    def __init__(self) -> None:
        pass
    
    # put chars for encoding
    def forced_url_encoding(self, payload):
        # encoding 할 문자 입력(list)
        characters = ['<', '>', ' ', '%', '"']

        # 리스트 내 문자 뽑아서encode them using URL encoding
        for char in characters:
            payload = payload.replace(char, "%" + format(ord(char), 'x'))

        return payload

    
    # # put chars for decoding
    def forced_url_decoding(self, payload):
        # split the payload into separate components
        components = payload.split("%")

        # loop through the components and decode them using URL decoding
        decoded_payload = components[0]
        for component in components[1:]:
            decoded_payload += chr(int(component[:2], 16)) + component[2:]

        return decoded_payload

if __name__ == '__main__':
    um = URL_Modifier()
    
    # testcase1
    payload = '<script>alert("XSS")</script>'
    encoded_payload = um.forced_url_encoding(payload)
    print("Encoded payload: ", encoded_payload)

    # testcase2
    payload = '%3Cscript%3Ealert%28%22XSS%22%29%3C%2Fscript%3E'
    decoded_payload = um.forced_url_decoding(payload)
    print("Decoded payload: ", decoded_payload)