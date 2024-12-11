from psychopy.event import waitKeys

def wait_three_keys(key1, key2, key3):
    response1 = waitKeys(keyList=[key1])[0]
    response2 = waitKeys(keyList=[key2])[0]
    response3 = waitKeys(keyList=[key3])[0]
    return response1, response2, response3
