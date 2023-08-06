STATS_COLUMNS = ['PTS', 'FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'AST', 'STL', 'BLK', 'TOV', 'PF']

OPP_STATS_COLUMNS = [f"{col}_OPP" for col in STATS_COLUMNS]

FEATURE_COLUMNS = [f'OPP_{stat}' for stat in STATS_COLUMNS + OPP_STATS_COLUMNS] + ['HOME']