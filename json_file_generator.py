from json import dump, load

def generate(mode):
    lstats = {"Correct": 0,
          "Answered": 0,
          "Time": 0}

    with open(f"lifetime_stats\{mode}lifetime_stats.json", "w") as stats:
        dump(lstats, stats)

def update_stats(mode, new):
    statfile = f"lifetime_stats\{mode}lifetime_stats.json"
    stats = {}
    try:
        with open(statfile, "r") as stats_dict:
            stats = load(stats_dict)
    
    except FileNotFoundError:
        generate(mode)
        with open(statfile, "r") as stats_dict:
            stats = load(stats_dict)

    for i in stats.keys():
        stats[i] += new[i]
        
    with open(statfile, "w") as stats_dict:
        dump(stats, stats_dict)