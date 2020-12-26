def game_to_genre(game_name):
    genres_dict = {}
    with open('genres_dict.txt', 'r') as file:
        file.seek(0)
        for line in file:
            stripped_line = line.strip()
            key, *value = stripped_line.split(', ')
            genres_dict[key] = value
    game_genre = None
    lowered_game_name = game_name.strip().lower()
    for key, value in genres_dict.items():
        if lowered_game_name in value:
            game_genre = key
            return game_genre
    if game_genre is None:
        print('\nThe game is not found. Where would you like to add it?\n'
              '- MOBA\n'
              '- FPS\n'
              '- MMORPG\n'
              '- STRATEGY\n')
        new_game_input = input().upper()
        genres_dict[new_game_input].append(lowered_game_name)
        with open('genres_dict.txt', 'w') as file:
            file.seek(0)
            for key, value in genres_dict.items():
                file.write('{}'.format(key))
                for i in value:
                    file.write(', {}'.format(i))
                file.write('\n')
        return 'Completed!'


name = input()
print(game_to_genre(name))
