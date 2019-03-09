def read_card():
    result = None
    (stat, tag_type) = card_reader.request(card_reader.REQIDL)
    if stat == card_reader.OK:
        (stat, raw_uid) = card_reader.anticoll()
        if stat == card_reader.OK:
            tag_type_str = "0x{:02x}".format(tag_type)
            uid_string = "0x{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            if card_reader.select_tag(raw_uid) == card_reader.OK:
                key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                if card_reader.auth(card_reader.AUTHENT1A, 8, key, raw_uid) == card_reader.OK:
                    payload = "{}".format(str(card_reader.read(8)))
                    card_reader.stop_crypto1()
                    result = {
                        "TagType" : tag_type_str,
                        "UID" : uid_string,
                        "Payload" : payload
                    }
    return result

def send_data(data):
    print("Card Type:\t", data["TagType"])
    print("Card Uid:\t", data["UID"])
    print("Payload:\t", data["Payload"], '\n')

def blink(count, duration_ms):
    phases = 2 * count - 1
    for i in range(phases):
        led.value(0 if led.value() > 0 else 1)
        time.sleep_ms(int(duration_ms / phases))

def run():
    last_uid = None
    count = 0
    while True:
        data = read_card()
        if data is not None:
            if data["UID"] is not last_uid:
                send_data(data)
                blink(3,1500)
                last_uid = data["UID"]
            count = 99
        if count < 0 and last_uid is not None:
            last_uid = None
        else:
            count -= 1
            
