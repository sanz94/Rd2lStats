
# Contains the current week match ID's to parse stats for
match_ids = ["6475422949", "6475464700", "6475417352", "6475457055", "6475425285", "6475464729", "6475470216", "6475422475", "6475466598", "6475418086", "6475451619", "6475419737", "6475445676", "6475426863", "6475468599", "6475420100", "6475455996", "6475421631", "6475458588"]
week6matches = ["6464328817", "6464364627", "6464328217", "6464368358", "6464326758", "6464365475", "6464332812", "6464359926", "6464329160", "6464376238", "6464328534", "6464360517", "6464325893", "6464361794", "6464328585", "6464370005", "6464331721", "6464377762", "6464327212", "6464361940"]
week5matches = ["6453768878", "6453809302", "6453806404", "6453769511", "6453797730", "6453806546", "6453767326", "6453806176", "6453770297", "6453771686", "6453805772", "6453812638", "6453767670", "6453765534", "6453794352", "6453811126", "6453767734"]
week4matches = ["6442337208", "6442340533", "6442374644", "6442384483", "6442392229", "6442339747", "6442369562", "6442336462", "6442372668", "6442339180", "6442372121", "6442336463", "6442385345", "6442340814", "6442380377"]
current_week = 4

# permissionkey location - added in manually
permissionkeyfile = "../permissionkey.txt"

# Used for fetching Hero icon images in embeds
steam_cdn = "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/"

# Dotabuff base URL
dotabuff_url = "https://www.dotabuff.com/matches/"

# Opendota API URL
opendota_api_players_url = "https://api.opendota.com/api/players/"
opendota_api_matches_url = "https://api.opendota.com/api/matches/"

# Stats multipliers, these are slightly modified from Dota's fantasy point calculation
fantasy_kill_multiplier = 0.5
fantasy_death_multiplier = -0.5
fantasy_assist_multiplier = 0.3
fantasy_lasthit_multiplier = 0.003
fantasy_gpm_multiplier = 0.002
fantasy_ts_multiplier = 1
fantasy_roshan_multiplier = 1
fantasy_wards_planted = 0.1
fantasy_wards_dewarded = 0.3
fantasy_camps_stacked = 0.4
fantasy_runes_grabbed = 0.2
fantasy_first_blood = 4
fantasy_stuns_multiplier = 0.05

# Pos 1 constants
pos1directory = "../pos1stats/"
pos1currentdirectory = "../current_week_stats/pos1stats/"
pos1gpmfile = "pos1gpmLeaderboard.csv"
pos1kdafile = "pos1kdaLeaderboard.csv"
pos1fantasyfile = "pos1fantasyLeaderboard.csv"

# Pos 2 constants
pos2directory = "../pos2stats/"
pos2currentdirectory = "../current_week_stats/pos2stats/"
pos2gpmfile = "pos2gpmLeaderboard.csv"
pos2kdafile = "pos2kdaLeaderboard.csv"
pos2fantasyfile = "pos2fantasyLeaderboard.csv"

# Pos 3 constants
pos3directory = "../pos3stats/"
pos3currentdirectory = "../current_week_stats/pos3stats/"
pos3gpmfile = "pos3gpmLeaderboard.csv"
pos3kdafile = "pos3kdaLeaderboard.csv"
pos3fantasyfile = "pos3fantasyLeaderboard.csv"

# Pos 4 constants
pos4directory = "../pos4stats/"
pos4currentdirectory = "../current_week_stats/pos4stats/"
pos4gpmfile = "pos4gpmLeaderboard.csv"
pos4kdafile = "pos4kdaLeaderboard.csv"
pos4fantasyfile = "pos4fantasyLeaderboard.csv"

# Pos 5 constants
pos5directory = "../pos5stats/"
pos5currentdirectory = "../current_week_stats/pos5stats/"
pos5gpmfile = "pos5gpmLeaderboard.csv"
pos5kdafile = "pos5kdaLeaderboard.csv"
pos5fantasyfile = "pos5fantasyLeaderboard.csv"
