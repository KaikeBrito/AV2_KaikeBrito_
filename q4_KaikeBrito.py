Users = ("Users", "u", ["id", "nome", "country", "id_console"])
VideoGames = ("VideoGames", "v", ["id_console", "nome", "id_company", "release_date"])
Games = ("Games", "g", ["id_game", "title", "genre", "release_date", "id_console"])
Company = ("Company", "c", ["id_company", "nome", "country"])

gen_inner_join = (
    lambda t1, t2: f"SELECT {', '.join(t1[1] + '.' + attr for attr in t1[2])}, "
    + f"{', '.join(t2[1] + '.' + attr for attr in t2[2])} "
    + f"FROM {t1[0]} AS {t1[1]} "
    + f"INNER JOIN {t2[0]} AS {t2[1]} ON {t1[1]}.id_console = {t2[1]}.id_console;"
)


gen_inner_join_users_videogames_games = (
    lambda t1, t2, t3: f"SELECT {', '.join(t1[1] + '.' + attr for attr in t1[2])}, "
    + f"{', '.join(t2[1] + '.' + attr for attr in t2[2])}, "
    + f"{', '.join(t3[1] + '.' + attr for attr in t3[2])} "
    + f"FROM {t1[0]} AS {t1[1]} "
    + f"INNER JOIN {t2[0]} AS {t2[1]} ON {t1[1]}.id_console = {t2[1]}.id_console "
    + f"INNER JOIN {t3[0]} AS {t3[1]} ON {t2[1]}.id_console = {t3[1]}.id_console;"
)

gen_inner_join_company_videogames_games = (
    lambda t1, t2, t3: f"SELECT {', '.join(t1[1] + '.' + attr for attr in t1[2])}, "
    + f"{', '.join(t2[1] + '.' + attr for attr in t2[2])}, "
    + f"{', '.join(t3[1] + '.' + attr for attr in t3[2])} "
    + f"FROM {t1[0]} AS {t1[1]} "
    + f"INNER JOIN {t2[0]} AS {t2[1]} ON {t1[1]}.id_company = {t2[1]}.id_company "
    + f"INNER JOIN {t3[0]} AS {t3[1]} ON {t2[1]}.id_console = {t3[1]}.id_console;"
)


join_users_videogames = lambda: gen_inner_join(Users, VideoGames)
join_videogames_games = lambda: gen_inner_join(VideoGames, Games)
join_videogames_company = lambda: gen_inner_join(VideoGames, Company)

inner_join_query = lambda: gen_inner_join_users_videogames_games(Users, VideoGames, Games)
print(inner_join_query())

inner_join_query_2 = lambda: gen_inner_join_company_videogames_games(Company, VideoGames, Games)
print(inner_join_query_2())

print(join_videogames_games())  