if __name__ == "__main__":
    print("Problem 1 - Song Popularity:")
    score = calculate_song_popularity(5000, 150, 25)
    print(f"Popularity score: {score}")
    print()

    print("Problem 2 - Total Listening Time:")
    durations = [180, 210, 195, 240]
    total = total_listening_time(durations)
    print(f"Total time: {total} seconds")
    print()

    print("Problem 3 - Extend Songs:")
    original = [180, 210, 195]
    new_list = extend_songs_immutable(original)
    print(f"Original (immutable): {original}")
    print(f"New list: {new_list}")

    mutable_list = [180, 210, 195]
    extend_song_mutable(mutable_list)
    print(f"Modified list (mutable): {mutable_list}")
    print()

    print("Problem 4 - Song Objects:")
    print(song1)
    print(song2)
    print(song3)