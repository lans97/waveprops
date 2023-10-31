from math import pi, log
c = 299792458

methods = ["okumura", "hata", "siu", "hata_extension", "walfisch_ikegami", "longley_rice", "free_space", "two_ray_ground", "okumura_hata", "erikson9999"]

def okumura():
    return 0

def hata(opt, f, hm, hb, d):
    if (opt == "urbanL" or opt == "urbanM" or opt == "urbanS"):
        return 69.55 + 26.16 * log(f, 10) - 13.82 * log(hb, 10) - h_a(opt, f, hm) + (44.9 - 6.55 * log(hb, 10)) * log(d, 10)
    if (opt == "suburban"):
        return hata("urbanM", f, hm , hb, d) - 2 * log(f/28, 10)**2 - 5.4
    if (opt == "open"):
        return hata("urbanS", f, hm, hb, d) - 4.78 * log(f, 10)**2 + 18.33 * log(f, 10) - 40.94
    return 0

def h_a(opt, f, hm):
    if (opt == "urbanM" or opt == "urbanS"):
        return 0.8 + (1.1 * log(f, 10) - 0.7) * hm - 1.56 * log(f, 10)
    if(opt == "urbanL"):
        if(150 <= f and f <= 200):
            return 8.29 * (log(1.54 * hm, 10))**2 - 1.1
        if(200 <= f and f <= 1500):
            return 3.2 * (log(11.75 * hm, 10))**2 - 4.97
    return 0

h_opts = ["urbanS", "urbanM", "urbanL", "suburban", "open"]

def siu():
    return 0

def hata_extension():
    return 0

def walfisch_ikegami():
    return 0

def longley_rice():
    return 0

def free_space():
    return 0

def two_ray_ground():
    return 0

def okumura_hata(opt, f, hm, hb, d):
    if (opt == "suburban" and (hm < 1 or hm > 10 )):
        return "err"

    res = 69.55 + 26.16 * log(f, 10) - 13.82 * log(hb - oh_a(opt, hm, f), 10) + (44.9 - 6.55 * log(hb, 10)) * log(d, 10)
    if (opt == 3):
        res -= (2 * log(f/28, 10)**2) - 5.4
    if (opt == 4):
        res -= (4.78 * log(f, 10)**2) + 18.33 * log(f, 10) - 40.94
    return res

def oh_a(opt, hm, f):
    if(opt == "suburban"):
        return oh_a_Suburban(hm, f)
    if (opt == "urban" or opt == "rural" or opt == "open"):
        return oh_a_Urban(hm, f)

def oh_a_Suburban(hm, f):
    if (hm < 1 or hm > 10):
        return 0
    return (1.1 * log(f, 10) - 0.7) * hm - (1.6 * log(f, 10) - 0.8)

def oh_a_Urban(hm, f):
    if (f > 200):
        return 3.2 * log(11.75 * hm, 10)**2 - 4.97

    return 8.29 * log(1.54 * hm, 10)**2 - 1.1

oh_opts = ["suburban", "urban", "rural", "open"]

def erikson9999():
    return 0
