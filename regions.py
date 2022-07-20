regoins = {'a': 'london', 'aa': 'bournemouth', 'ab':'worcester', 'ac':'coventry', 'ad': 'gloucester', 'ae': 'bristol', 'af': 'truro',
           'ag': 'hull', 'ah': 'norwich', 'aj': 'middlesbrough', 'ak': 'sheffield',
            'al': 'nottingham', 'am': 'swindon', 'an': 'reading', 'ao': 'carlisle', 'ap': 'brighton', 'ar': 'chelmsford', 'as': 'inverness',
            'at': 'hull', 'au': 'nottingham', 'av': 'peterborough', 'aw': 'shrewsbury', 'ax': 'cardiff', 'ay': 'leicester', 'az': 'belfast',
           'b': 'lancashire', 'ba': 'manchester', 'bb': 'newcastle-upon-tyne', 'bc': 'leicester', 'bd': 'northampton', 'be': 'lincoln', 'bf': 'stoke-on-trent',
           'bg': 'liverpool', 'bh': 'luton','bj': 'ipswich', 'bk': 'portsmouth', 'bl': 'reading', 'bm': 'luton', 'bn': 'manchester', 'or': 'bolton', 'bo': 'cardiff',
           'bp': 'portsmouth', 'br': 'newcastle-upon-tyne', 'bs': 'aberdeen bt leeds bu manchester', 'bv': 'preston', 'bw': 'oxford', 'bx': 'haverfordwest',
           'by': 'london (north-west)', 'bz': 'county down', 'c': 'west yorkshire', 'ca': 'chester', 'cb': 'manchester', 'cc': 'bangor', 'cd': 'brighton', 'ce': 'peterborough',
           'cf': 'reading', 'cg': 'bournemouth', 'ch': 'nottingham', 'cj': 'gloucester','ck': 'preston', 'cl': 'norwich', 'cm': 'liverpool', 'cn': 'newcastle-upon-tyne', 'co': 'exeter',
           'cp': 'huddersfield', 'cr': 'southampton','cs': 'glasgow', 'ct': 'lincoln', 'cu': 'newcastle-upon-tyne', 'cv': 'truro', 'cw': 'preston', 'cx': 'huddersfield', 'cy': 'swansea',
           'cz': 'belfast', 'd': 'kent', 'da': 'birmingham', 'db': 'manchester', 'dc': 'middlesbrough','dd': 'gloucester', 'de': 'haverfordwest', 'df': 'gloucester', 'dg': 'gloucester', 'dh': 'dudley', 'dj': 'liverpool',
           'dk': 'rochdale later manchester', 'dl': 'portsmouth', 'dm': 'chester', 'dn': 'leeds', 'do': 'lincoln', 'dp': 'reading', 'dr': 'exeter', 'ds': 'glasgow', 'dt': 'sheffield',
           'du': 'coventry', 'dv': 'exeter', 'dw':'cardiff', 'dx': 'ipswich', 'dy': 'brighton', 'dz': 'county antrim', 'e': 'staffordshire', 'ea': 'dudley', 'eb': 'peterborough',
           'ec': 'preston', 'ed': 'liverpool', 'ee': 'lincoln', 'ef': 'middlesbrough', 'eg': 'peterborough', 'eh': 'stoke-on-trent', 'ej': 'haverfordwest', 'ek': 'liverpool',
           'el': 'bournemouth', 'em': 'liverpool', 'en': 'bury later manchester', 'eo': 'preston', 'ep': 'swansea', 'er': 'peterborough', 'es': 'dundee', 'et': 'sheffield', 'eu': 'bristol',
           'ev': 'chelmsford', 'ew': 'peterborough', 'ex': 'norwich', 'ey': 'bangor', 'ez': 'belfast', 'f': 'essex', 'fa': 'stoke-on-trent', 'fb': 'bristol', 'fc': 'oxford', 'fd': 'dudley',
           'fe': 'lincoln', 'ff': 'bangor', 'fg': 'brighton', 'fh': 'gloucester', 'fj': 'exeter', 'fk': 'dudley', 'fl': 'peterborough', 'fm': 'chester',
           'fn': 'maidstone', 'fo': 'gloucester', 'fp': 'leicester', 'fr': 'preston', 'fs': 'edinburgh', 'ft': 'newcastle-upon-tyne', 'fu': 'lincoln', 'fv': 'preston', 'fw': 'lincoln',  'fx': 'bournemouth',
           'fy': 'liverpool', 'fz': 'belfast','g': 'glasgow', 'ga': 'glasgow', 'gb': 'glasgow','gc':'london (south-west)','gd': 'glasgow', 'ge': 'glasgow', 'gf': 'london (south-west)', 'gg': 'glasgow',
           'gh': 'london (south-west)', 'gj': 'london (south-west)','gk': 'london (south-west)', 'gl': 'truro', 'gm': 'reading', 'gn': 'london (south-west)', 'go': 'london (south-west)', 'gp': 'london (south-west)', 'gr': 'newcastle-upon-tyne',
           'gs': 'luton','gt': 'london (south-west)', 'gu': 'london (south-east)', 'gv': 'ipswich', 'gw': 'london (south-east)', 'gx': 'london (south-east)', 'gy':'london (south-east)', 'gz': 'belfast',
           'h': 'london', 'ha': 'dudley', 'hb': 'cardiff', 'hc': 'brighton', 'hd': 'huddersfield', 'he': 'sheffield', 'hf': 'liverpool', 'hg': 'preston', 'hh': 'carlisle', 'hj': 'chelmsford', 'hk': 'chelmsford',
           'hl': 'sheffield','hm': 'london (central)','hn': 'middlesbrough', 'ho': 'bournemouth', 'hp': 'coventry', 'hr': 'swindon', 'hs': 'glasgow', 'ht': 'bristol', 'hu': 'bristol','hv': 'london (central)'
           ,'hw': 'bristol', 'hx': 'london (central)', 'hy': 'bristol', 'j': 'durham','ja': 'manchester', 'jb': 'reading', 'jc': 'bangor', 'jd': 'london (central)', 'je': 'peterborough', 'jf': 'leicester',
           'jg': 'maidstone', 'jh': 'reading', 'jj': 'maidstone', 'jk': 'brighton', 'jl': 'lincoln', 'jm': 'reading','jn': 'chelmsford', 'jo': 'oxford', 'jp': 'liverpool', 'jr': 'newcastle-upon-tyne', 'js': 'inverness', 'jt': 'bournemouth', 'ju': 'leicester',
           'jv': 'lincoln', 'jw': 'birmingham', 'jx': 'huddersfield', 'jy': 'exeter','jz': 'county down', 'k': 'liverpool', 'ka': 'liverpool', 'kb': 'liverpool', 'kc': 'liverpool', 'kd': 'liverpool', 'ke': 'maidstone', 'kf': 'liverpool', 'kg': 'cardiff', 'kh': 'hull', 'kj': 'maidstone', 'kk': 'maidstone',
           'kl': 'maidstone', 'km': 'maidstone', 'kn': 'maidstone', 'ko': 'maidstone', 'kp': 'maidstone', 'kr': 'maidstone', 'ks': 'edinburgh', 'kt': 'maidstone', 'ku': 'sheffield', 'kv': 'coventry', 'kw': 'sheffield', 'kx': 'luton',
           'ky': 'sheffield', 'kz': 'county antrim', 'l': 'glamorganshire', 'la': 'london (north-west) (used for london county council before 1965)', 'lb': 'london (north-west) (used for london county council before 1965)',
'lc': 'london (north-west) (used for london county council before 1965)', 'ld': 'london (north-west) (used for london county council before 1965)',
'le': 'london (north-west) (used for london county council before 1965)', 'lf': 'london (north-west) (used for london county council before 1965)',
'lg': 'chester lh london (north-west) (used for london county council before 1965)', 'kj': 'bournemouth', 'lk': 'london (north-west) (used for london county council before 1965)',
'll': 'london (north-west) (used for london county council before 1965)', 'lm': 'london (north-west) (used for london county council before 1965)',
'ln': 'london (north-west) (used for london county council before 1965)', 'lo': 'london (north-west) (used for london county council before 1965)',
'lp': 'london (north-west) (used for london county council before 1965)', 'lr': 'london (north-west) (used for london county council before 1965)',
'ls': 'edinburgh', 'lt': 'london (north-west) (used for london county council before 1965)', 'lu': 'london (north-west) (used for london county council before 1965)',
'lv': 'liverpool', 'lw': 'london (north-west) (used for london county council before 1965)', 'lx': 'london (north-west) (used for london county council before 1965)',
'ly': 'london (north-west) (used for london county council before 1965)', 'lz': 'county armagh', 'm': 'cheshire', 'ma': 'chester', 'mb': 'chester', 'mc': 'london (north-east) (used for middlesex before 1965)',
'md': 'london (north-east) (used for middlesex before 1965)', 'me': 'london (north-east) (used for middlesex before 1965)', 'mf': 'london (north-east) (used for middlesex before 1965)',
'mg': 'london (north-east) (used for middlesex before 1965)', 'mh': 'london (north-east) (used for middlesex before 1965)', 'mj': 'luton', 'mk': 'london (north-east)(used for middlesex before 1965)',
'ml': 'london (north-east) (used for middlesex before 1965)', 'mm': 'london (north-east) (used for middlesex before 1965)',
'mn': 'used in the isle of man', 'mo': 'reading', 'mp': 'london (north-east) (used for middlesex before 1965)', 'mr': 'swindon', 'ms': 'edinburgh', 'mt': 'london (north-east) (used for middlesex before 1965)',
'mu': 'london (north-east) (used for middlesex before 1965)', 'mv': 'london (north-east) (used for middlesex before 1965)', 'mw': 'swindon', 'mx': 'london (north-east) (used for middlesex before 1965)',
'my': 'london (north-east) (used for middlesex before 1965)', 'mz': 'belfast', 'n': 'manchester', 'na': 'manchester', 'nb': 'manchester', 'nc': 'manchester', 'nd': 'manchester', 'ne': 'manchester', 'nf': 'manchester',
'ng': 'norwich', 'nh': 'northampton', 'nj': 'brighton', 'nk': 'luton', 'nl': 'newcastle-upon-tyne', 'nm': 'luton', 'nn': 'nottingham', 'no': 'chelmsford', 'np': 'worcester', 'nr': 'leicester', 'ns': 'glasgow', 'nt': 'shrewsbury',
'nu': 'nottingham','nv': 'northampton', 'nw': 'leeds', 'nx': 'dudley', 'ny': 'cardiff', 'nz': 'county londonderry/derry', 'o': 'birmingham', 'oa': 'birmingham', 'ob': 'birmingham', 'oc': 'birmingham', 'od': 'exeter', 'oe': 'birmingham',
'of': 'birmingham','og': 'birmingham', 'oh': 'birmingham',  'oi': 'belfast', 'oj': 'birmingham', 'ok': 'birmingham', 'ol': 'birmingham', 'om': 'birmingham', 'on': 'birmingham', 'oo': 'chelmsford', 'op': 'birmingham', 'or': 'portsmouth',
'os': 'glasgow', 'ot': 'portsmouth', 'ou': 'bristol', 'ov': 'birmingham', 'ow': 'southampton', 'ox': 'birmingham', 'oy': 'london (north-west)', 'oz': 'belfast', 'p': 'surrey', 'pa': 'guildford', 'pb': 'guildford', 'pc': 'guildford',
           'pd': 'guildford','pe': 'guildford', 'pf': 'guildford', 'pg': 'guildford', 'ph': 'guildford', 'pj': 'guildford', 'pk': 'guildford', 'pl': 'guildford', 'pm': 'guildford', 'pn': 'brighton', 'po': 'portsmouth (gpo formerly used for general post office vehicles)',
'pp': 'luton', 'pr': 'bournemouth', 'ps': 'aberdeen', 'pt': 'newcastle-upon-tyne', 'pu': 'chelmsford', 'pv': 'ipswich', 'pw': 'norwich', 'px': 'portsmouth', 'py': 'middlesbrough', 'pz': 'belfast', 'r': 'derbyshire', 'ra': 'nottingham',
'rb': 'nottingham', 'rc': 'nottingham', 'rd': 'reading', 're': 'stoke-on-trent', 'rf': 'stoke-on-trent', 'rg': 'newcastle-upon-tyne', 'rh': 'hull', 'rj': 'manchester', 'rk': 'london (north-west)', 'rl': 'truro', 'rm': 'carlisle',
'rn': 'preston', 'ro': 'luton', 'rp': 'northampton', 'rr': 'nottingham', 'rs': 'aberdeen', 'rt': 'ipswich', 'ru': 'bournemouth', 'rv': 'portsmouth', 'rw': 'coventry', 'rx': 'reading', 'ry': 'leicester', 'rz': 'county antrim', 's': 'edinburgh',
'sa': 'aberdeen', 'sb': 'glasgow', 'sc': 'edinburgh', 'sd': 'glasgow', 'se': 'aberdeen', 'sf': 'edinburgh', 'sg': 'edinburgh', 'sh': 'edinburgh', 'sj': 'glasgow', 'sk': 'inverness', 'sl': 'dundee', 'sm': 'carlisle', 'sn': 'dundee', 'so': 'aberdeen',
'sp': 'dundee', 'sr': 'dundee', 'ss': 'aberdeen', 'st': 'inverness', 'su': 'glasgow', 'sw': 'carlisle', 'sx': 'edinburgh', 't': 'devon', 'ta': 'exeter', 'tb': 'liverpool', 'tc': 'bristol', 'td': 'manchester', 'te': 'manchester', 'tf': 'reading',
'tg': 'cardiff', 'th': 'swansea', 'tj': 'liverpool', 'tk': 'exeter', 'tl': 'lincoln', 'tm': 'luton', 'tn': 'newcastle-upon-tyne', 'to': 'nottingham', 'tp': 'portsmouth', 'tr': 'southampton', 'ts': 'dundee', 'tt': 'exeter', 'tu': 'chester',
'tv': 'nottingham', 'tw': 'chelmsford', 'tx': 'cardiff', 'ty': 'newcastle-upon-tyne', 'tz': 'belfast', 'u': 'leeds', 'ua': 'leeds', 'ub': 'leeds', 'uc': 'london (central)', 'ud': 'oxford', 'ue': 'dudley', 'uf': 'brighton', 'ug': 'leeds', 'uh': 'cardiff',
'ui': 'county londonderry/derry', 'uj': 'shrewsbury', 'uk': 'birmingham', 'ul': 'london (central)', 'um': 'leeds', 'un': 'exeter', 'uo': 'exeter', 'up': 'newcastle-upon-tyne', 'ur': 'luton', 'us': 'glasgow', 'ut': 'leicester',
'uu': 'london (central)', 'uv': 'london (central)', 'uw': 'london (central)', 'ux': 'shrewsbury', 'uy': 'worcester', 'uz': 'belfast', 'v': 'lanarkshire', 'va': 'peterborough', 'vb': 'maidstone', 'vc': 'coventry',
'vd': 'lanarkshire/luton', 've': 'peterborough', 'vf': 'norwich', 'vg': 'norwich', 'vh': 'huddersfield', 'vj': 'gloucester', 'vk': 'newcastle-upon-tyne', 'vl': 'lincoln', 'vm': 'manchester', 'vn': 'middlesbrough',
'vo': 'nottingham', 'vp': 'birmingham', 'vr': 'manchester', 'vs': 'luton', 'vt': 'stoke-on-trent', 'vu': 'manchester', 'vv': 'northampton', 'vw': 'chelmsford', 'vx': 'chelmsford', 'vy': 'leeds', 'vz': 'county tyrone', 'w': 'sheffield',
'wa': 'sheffield', 'wb': 'sheffield', 'wc': 'chelmsford', 'wd': 'dudley', 'we': 'sheffield', 'wf': 'sheffield', 'wg': 'sheffield', 'wh': 'manchester', 'or': 'bolton', 'wj': 'sheffield', 'wk': 'coventry', 'wl': 'oxford', 'wm': 'liverpool',
'wn': 'swansea', 'wo': 'cardiff', 'wp': 'worcester', 'wr': 'leeds', 'ws': 'bristol', 'wt': 'leeds', 'wu': 'leeds', 'wv': 'brighton', 'ww': 'leeds', 'wx': 'leeds', 'wy': 'leeds', 'wz': 'belfast', 'x': 'northumberland', 'xi': 'belfast', 'xz': 'county armagh',
'y': 'somerset', 'ya': 'taunton', 'yb': 'taunton', 'yc': 'taunton', 'yd': 'taunton', 'ye': 'london (central)', 'yf': 'london (central)', 'yg': 'leeds', 'yh': 'london (central)', 'yj': 'brighton', 'yk': 'london (central)',
'yl': 'london (central)', 'ym': 'london (central)', 'yn': 'london (central)', 'yo': 'london (central)', 'yp': 'london (central)', 'yr': 'london (central)', 'ys': 'glasgow', 'yt': 'london (central)', 'yu': 'london (central)',
'yv': 'london (central)', 'yw': 'london (central)', 'yx': 'london (central)', 'yy': 'london (central)', 'yz': 'county londonderry'}