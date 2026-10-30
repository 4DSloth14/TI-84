import math
from ti_system import recall_list

L1 = recall_list("1")   # read but not used in stats
L2 = recall_list("2")
L3 = recall_list("3")
L4 = recall_list("4")

def sig_count(x):
    # Count significant digits in a value's text form
    s = str(abs(x))
    if "e" in s:
        s = s.split("e")
    s = s.replace(".", "").lstrip("0")
    return max(len(s), 1)

def round_sig(x, n):
    if x == 0:
        return 0.0
    return round(x, n - int(math.floor(math.log10(abs(x)))) - 1)

def stats(data):
    n = len(data)
    mean = sum(data) / n
    s = sorted(data)
    if n % 2 == 1:
        median = s[n // 2]
    else:
        median = (s[n // 2 - 1] + s[n // 2]) / 2
    sd = math.sqrt(sum((x - mean) ** 2 for x in data) / n)  # population SD
    return mean, median, sd

rows = []
for name, data in [("L2", L2), ("L3", L3), ("L4", L4)]:
    if len(data) == 0:
        rows.append((name, "empty", "empty", "empty"))
        continue
    # Use the fewest sig figs found in the list's entries
    n_sig = min(sig_count(x) for x in data)
    mean, median, sd = stats(data)
    rows.append((name,
                 round_sig(mean, n_sig),
                 round_sig(median, n_sig),
                 round_sig(sd, n_sig)))

print("List Mean    Median  SD")
for name, m, md, sd in rows:
    print(f"{name:<5}{str(m):<8}{str(md):<8}{sd}")
