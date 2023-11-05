"""
Write a Python code with the following criteria.

The Python script organizes video game titles into categories in a list of dictionaries and prints them, with the output neatly formatted to display each category followed by its games. 
It utilizes f-strings for dynamic insertion of data during iteration for a clear, categorized presentation of titles.
"""

video_games = [
    {
        "category": "Action",
        "video_game_titles": ["Call of Duty", "Fortnite", "Assassin's Creed"]
    },
    {
        "category": "Adventure",
        "video_game_titles": ["The Legend of Zelda: Breath of the Wild", "Uncharted 4: A Thief's End", "Tomb Raider"]
    },
    {
        "category": "Sports",
        "video_game_titles": ["FIFA 21", "NBA 2K21", "Madden NFL 21"]
    }
]


for category in video_games:
    print(f"\n-------Category:{category['category']}-------\n")
    for video_game in category["video_game_titles"]:
        print(
            f"Video game title: {video_game}")
