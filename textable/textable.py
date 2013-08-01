
def numplaces(num, uncert=False):
    if uncert:
        l, r = '{}'.format(num).split('+/-')
        a, b = l.split('.')
        c, d = r.split('.')
        return len(a), len(b), len(d)
    else:
        # TODO temporary hack
        a, b = '{:.1f}'.format(num).split('.')
        return len(a), len(b)

def is_uncert(num):
    uncert = True
    try:
        num.nominal_value
        num.std_dev
    except:
        uncert = False
    return uncert

def genspec(col):
    amax = 0
    bmax = 0
    cmax = 0
    for v in col:
        if is_uncert(v):
            v.nominal_value
            v.std_dev
            a, b, c = numplaces(v, uncert=True)
            if a > amax:
                amax = a
            if b > bmax:
                bmax = b
            if c > cmax:
                cmax = c
        else:
            a, b = numplaces(v)
            if a > amax:
                amax = a
            if b > bmax:
                bmax = b
    if cmax:
        return 'S[table-format={}.{}({})]'.format(amax, bmax, cmax)
    else:
        return 'S[table-format={}.{}]'.format(amax, bmax)

def table(names, cols):
    result = []

    spec = ' '.join(map(genspec, cols))

    result.append(r'\begin{{tabular}}{{{}}}'.format(spec))
    result.append(r'\toprule')
    result.append(' & '.join(map(r'\multicolumn{{1}}{{c}}{{{}}}'.format, names)) + r'\\')
    result.append(r'\midrule')

    line = []
    maxlen = 0
    for c in cols:
        maxlen = max(len(c), maxlen)
    for i in range(maxlen):
        for c in cols:
            try:
                if is_uncert(c[i]):
                    line.append('{:L}'.format(c[i]))
                else:
                    line.append('{}'.format(c[i]))
            except:
                line.append('')
        result.append(' & '.join(line) + r' \\')
        line = []

    result.append(r'\bottomrule')
    result.append(r'\end{tabular}')

    return '\n'.join(result)

