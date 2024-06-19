import json

def print_json_structure(data, indent=0):
    """
    Recursively prints the keys of a JSON object.
    
    :param data: The JSON data (dictionary or list)
    :param indent: The current indentation level (used for nested structures)
    """
    indent_str = ' ' * indent
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{indent_str}{key}")
            if isinstance(value, (dict, list)):
                print_json_structure(value, indent + 4)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print(f"{indent_str}[{index}]")
            if isinstance(item, (dict, list)):
                print_json_structure(item, indent + 4)

def main():
    # Example large JSON string from scraper
    large_json_string = '''
    {'thread': {'text': 'No one loves a drop-in dinner guest… especially if you’re the dinner 😮\u200d💨😳 The Flood is streaming on Disney+', 'published_on': 1718211770, 'id': '3388928313420694692_787132', 'pk': '3388928313420694692', 'code': 'C8H5FiCtESk', 'username': 'natgeo', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/445315924_1179476269899767_3812682513517013106_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=1&_nc_ohc=DaVYET1OpxoQ7kNvgHn2kH6&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYD8oqkADrFX80ncNmPp6hflyePB6wGPXEtmLtFu-eQoNA&oe=66780F84&_nc_sid=10d13b', 'user_verified': True, 'user_pk': '787132', 'user_id': None, 'has_audio': True, 'reply_count': None, 'like_count': 1427, 'images': None, 'image_count': None, 'videos': ['https://scontent.cdninstagram.com/o1/v/t16/f2/m69/An_0DAta0xzS30UE2VmywTHuEsCdooQ36-399rjc5R8NwrHhSwKMIlrhGZbqtK1YKBqfc_ZzwwXbVQ9fHfp94jVc.mp4?efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uZmVlZC5jMi4xMDgwLmhpZ2gifQ&_nc_ht=scontent.cdninstagram.com&_nc_cat=106&vs=788544609927205_192864873&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HR0dNU0FmS09hX3YyaWtFQU10THpLQVFPZ2Q0YnBSMUFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dPeHh0aHBJcHctREJ2WURBR3I1MUhtMEFaWTZia1lMQUFBRhUCAsgBACgAGAAbABUAACaA7%2BHXyJCBQBUCKAJDMywXQCwzMzMzMzMYEmRhc2hfaGlnaF8xMDgwcF92MREAdeoHAA%3D%3D&ccb=9-4&oh=00_AYABIkfgGy0SxW5F0StrIU06P1Qc8rK_xxmbJ1BBpe9yng&oe=6674387A&_nc_sid=10d13b'], 'url': 'https://www.threads.net/@natgeo/post/C8H5FiCtESk'}, 'replies': [{'text': 'Que video tan triste 😢😢😢😢', 'published_on': 1718327761, 'id': '3389901420562455693_53720788839', 'pk': '3389901420562455693', 'code': 'C8LWWGsN5yN', 'username': 'marthasanchez9246', 'user_pic': 'https://instagram.fsub8-2.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fsub8-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=d38vMPEBHWwQ7kNvgH5Q0yo&edm=AJ9x6zYBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AYBlJKOv14EZCvIVjybTCdFmgnsvyAZiSaYE43a9L9RS_g&oe=6677F58F&_nc_sid=65462d', 'user_verified': False, 'user_pk': '53720788839', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@marthasanchez9246/post/C8LWWGsN5yN'}, {'text': '❤️❤️❤️❤️ leopards', 'published_on': 1718228343, 'id': '3389067442251486126_1916114270', 'pk': '3389067442251486126', 'code': 'C8IYuH3PdOu', 'username': 'altia58', 'user_pic': 'https://instagram.fsub8-2.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fsub8-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=d38vMPEBHWwQ7kNvgH5Q0yo&edm=AJ9x6zYBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AYBlJKOv14EZCvIVjybTCdFmgnsvyAZiSaYE43a9L9RS_g&oe=6677F58F&_nc_sid=65462d', 'user_verified': False, 'user_pk': '1916114270', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@altia58/post/C8IYuH3PdOu'}, {'text': 'Crazy height', 'published_on': 1718269599, 'id': '3389413516270515095_16006994536', 'pk': '3389413516270515095', 'code': 'C8JnaKaNjOX', 'username': 'adreanliegel', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/447952512_957142459229378_6965625641748334900_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=102&_nc_ohc=32LMz0m864YQ7kNvgEvr7ng&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYBi7xoUO67rj3gCEB99sf5pPengbseYZ5xzfX8y9YUR4A&oe=66780EF7&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '16006994536', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@adreanliegel/post/C8JnaKaNjOX'}, {'text': 'Hooooo', 'published_on': 1718317155, 'id': '3389812452915697009_5477077924', 'pk': '3389812452915697009', 'code': 'C8LCHdHPFVx', 'username': 'wilibaldozendejas', 'user_pic': 'https://instagram.fsub8-2.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fsub8-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=d38vMPEBHWwQ7kNvgH5Q0yo&edm=AJ9x6zYBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AYBlJKOv14EZCvIVjybTCdFmgnsvyAZiSaYE43a9L9RS_g&oe=6677F58F&_nc_sid=65462d', 'user_verified': False, 'user_pk': '5477077924', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@wilibaldozendejas/post/C8LCHdHPFVx'}, {'text': 'Tertible! I hate that', 'published_on': 1718214963, 'id': '3388955200729403662_66301395512', 'pk': '3388955200729403662', 'code': 'C8H_MyzMFEO', 'username': 'angeladelegall', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/440757362_7797710526939749_7405240155894368649_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=105&_nc_ohc=_ojGynpS4jYQ7kNvgF9P1xA&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYD7DI-HhhtC86iUlkLs5RGGFHOt3I036rYgvsEEXD2hlw&oe=667812D5&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '66301395512', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@angeladelegall/post/C8H_MyzMFEO'}, {'text': "That's the circle of life 🙁", 'published_on': 1718212189, 'id': '3388931927540406137_37210109626', 'pk': '3388931927540406137', 'code': 'C8H56H9Bpd5', 'username': 'jushrsr', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/447623614_448078034495039_4255481124706970511_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=111&_nc_ohc=sWhPyrUDIucQ7kNvgEYNtpX&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYDwb3OBh9obh0RidMYi8YbVa8LaiNyxhCg6n2kJ8CLpJA&oe=66780078&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '37210109626', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 1, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@jushrsr/post/C8H56H9Bpd5'}, {'text': 'Target', 'published_on': 1718307376, 'id': '3389730412991535954_50564975563', 'pk': '3389730412991535954', 'code': 'C8KvdnesttS', 'username': 'fancy70bonny', 'user_pic': 'https://instagram.fsub8-2.fna.fbcdn.net/v/t51.2885-19/44884218_345707102882519_2446069589734326272_n.jpg?_nc_ht=instagram.fsub8-2.fna.fbcdn.net&_nc_cat=1&_nc_ohc=d38vMPEBHWwQ7kNvgH5Q0yo&edm=AJ9x6zYBAAAA&ccb=7-5&ig_cache_key=YW5vbnltb3VzX3Byb2ZpbGVfcGlj.2-ccb7-5&oh=00_AYBlJKOv14EZCvIVjybTCdFmgnsvyAZiSaYE43a9L9RS_g&oe=6677F58F&_nc_sid=65462d', 'user_verified': False, 'user_pk': '50564975563', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@fancy70bonny/post/C8KvdnesttS'}, {'text': 'Hermoso, un buen cazador', 'published_on': 1718230287, 'id': '3389083748623819794_37211152220', 'pk': '3389083748623819794', 'code': 'C8IcbaWxaQS', 'username': 'rubi.osorio.9085', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/414205647_672296258441846_2890401772986035909_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=102&_nc_ohc=wyA-WRjDS00Q7kNvgHjTWEA&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYCwg5kJe1ecimn20pkT53NpqLIeoT-yMAhEzlfjk9VxnQ&oe=6677F90D&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '37211152220', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@rubi.osorio.9085/post/C8IcbaWxaQS'}, {'text': 'De life 🙈', 'published_on': 1718393551, 'id': '3390453308893287741_4522928581', 'pk': '3390453308893287741', 'code': 'C8NT1IwIdU9', 'username': 'manuela.bui', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/410718020_1075446220169049_1334613434954439772_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=109&_nc_ohc=WKM4JmGgFmgQ7kNvgETd11d&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYCESxGCCTpEkPf1GoCWv64yqh-lolXmbeIkGb0szmBsYw&oe=667801B2&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '4522928581', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@manuela.bui/post/C8NT1IwIdU9'}, {'text': '😲😲😲', 'published_on': 1718217825, 'id': '3388979205862780392_63544871719', 'pk': '3388979205862780392', 'code': 'C8IEqHUou3o', 'username': 'asc.1965', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/412039803_3731867570405274_1984055402343640206_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=106&_nc_ohc=um0VEvC9Y4oQ7kNvgH9i35D&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYDl4udVldjjaa_9UUtSZAnMntwFEKLQUolVdCgMBh76hw&oe=6677F6FC&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '63544871719', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@asc.1965/post/C8IEqHUou3o'}, {'text': '@katemaruyama when I get the portal working and drop in on you.', 'published_on': 1718228751, 'id': '3389070861972655617_54114044000', 'pk': '3389070861972655617', 'code': 'C8IZf4ugc4B', 'username': 'chikodiliemelumadu', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/446227765_1035315231287555_3346499231215470145_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=111&_nc_ohc=uJ_zwxQlI68Q7kNvgHiONdn&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYCk7K2CPcWzujrkFwr04XXK3piZaXq0LI4zX_1HHSYSWg&oe=6678293B&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '54114044000', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 1, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@chikodiliemelumadu/post/C8IZf4ugc4B'}, {'text': 'wow', 'published_on': 1718295100, 'id': '3389627437837282279_57060278629', 'pk': '3389627437837282279', 'code': 'C8KYDIZNWvn', 'username': 'petnarianpets', 'user_pic': 'https://scontent.cdninstagram.com/v/t51.2885-19/380903072_1029594291559865_6411506170395614098_n.jpg?stp=dst-jpg_s150x150&_nc_ht=scontent.cdninstagram.com&_nc_cat=105&_nc_ohc=Iq7iI2oWpx0Q7kNvgHTlsCj&edm=APs17CUBAAAA&ccb=7-5&oh=00_AYDVbAEFTtuague_kOMZ7EAysHYnkH2wuDLHDOcT5vnDZw&oe=6678055E&_nc_sid=10d13b', 'user_verified': False, 'user_pk': '57060278629', 'user_id': None, 'has_audio': None, 'reply_count': None, 'like_count': 0, 'images': None, 'image_count': None, 'videos': [], 'url': 'https://www.threads.net/@petnarianpets/post/C8KYDIZNWvn'}]}
    
    
    
    '''
    
    try:
        # Parse the JSON string into a Python dictionary
        json_data = json.loads(large_json_string)
        
        # Print the structure of the JSON data
        print("JSON Structure:")
        print_json_structure(json_data)
    
    except json.JSONDecodeError as e:
        print(f"Invalid JSON string: {e}")

if __name__ == "__main__":
    main()
