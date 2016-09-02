#!/usr/bin/env python
# encoding=utf-8

COUNTRIES = {'br': 'Brazil', 'pl': 'Poland', 'gt': 'Guatemala', 'mr': 'Mauritania',
             'ir': 'Iran, Islamic Republic of', 'ar': 'Argentina', 'ml': 'Mali', 'me': 'Montenegro',
             'et': 'Ethiopia', 'se': 'Sweden', 'ge': 'Georgia', 'td': 'Chad', 'eh': 'Western Sahara',
             'il': 'Israel', 'ng': 'Nigeria', 'cd': 'Congo, the Democratic Republic of the',
             'md': 'Moldova, Republic of', 'rw': 'Rwanda', 'kz': 'Kazakhstan', 'do': 'Dominican Republic',
             'bi': 'Burundi', 'ae': 'United Arab Emirates', 'in': 'India', 'ma': 'Morocco', 'cg': 'Congo',
             'mz': 'Mozambique', 'ke': 'Kenya', 'bw': 'Botswana', 'gq': 'Equatorial Guinea', 'ca': 'Canada',
             'mx': 'Mexico', 'ph': 'Philippines', 'sn': 'Senegal', 'aq': 'Antarctica', 'bh': 'Bahrain',
             'my': 'Malaysia', 'mw': 'Malawi', 'ec': 'Ecuador', 'dj': 'Djibouti', 'id': 'Indonesia',
             'py': 'Paraguay', 'de': 'Germany', 'ci': "Cote d'Ivoire", 'om': 'Oman', 'fr': 'France',
             'hu': 'Hungary', 'ps': 'Palestine, State of', 'gh': 'Ghana', 'cv': 'Cape Verde', 'so': 'Somalia',
             're': 'Reunion', 'ni': 'Nicaragua', 'gb': 'United Kingdom', 'iq': 'Iraq', 'mt': 'Malta',
             'vn': 'Viet Nam', 'ug': 'Uganda', 'ba': 'Bosnia and Herzegovina', 'cl': 'Chile', 'mn': 'Mongolia',
             'by': 'Belarus', 'li': 'Liechtenstein', 'tn': 'Tunisia', 'nz': 'New Zealand', 'co': 'Colombia',
             'sz': 'Swaziland', 'pe': 'Peru', 'bf': 'Burkina Faso', 'th': 'Thailand', 'am': 'Armenia',
             'mk': 'Macedonia, the former Yugoslav Republic of', 'np': 'Nepal', 'va': 'Holy See (Vatican City State)',
             'sd': 'Sudan', 'sh': 'Saint Helena, Ascension and Tristan da Cunha', 'ls': 'Lesotho', 'uz': 'Uzbekistan',
             'pa': 'Panama', 'gu': 'Guam', 'pg': 'Papua New Guinea', 'si': 'Slovenia', 'es': 'Spain', 'ua': 'Ukraine',
             'na': 'Namibia', 'ht': 'Haiti', 'af': 'Afghanistan', 'ly': 'Libyan Arab Jamahiriya', 've': 'Venezuela, Bolivarian Republic of',
             'sc': 'Seychelles', 'pr': 'Puerto Rico', 'kg': 'Kyrgyzstan', 'sg': 'Singapore', 'tg': 'Togo',
             'kp': "Korea, Democratic People's Republic of", 'be': 'Belgium', 'tz': 'Tanzania, United Republic of',
             'ao': 'Angola', 'lt': 'Lithuania', 'no': 'Norway', 'tj': 'Tajikistan', 'ro': 'Romania', 'cy': 'Cyprus',
             'sk': 'Slovakia', 'cm': 'Cameroon', 'ga': 'Gabon', 'ye': 'Yemen', 'jp': 'Japan', 'jm': 'Jamaica',
             'hk': 'Hong Kong', 'tw': 'Taiwan, Province of China', 'uy': 'Uruguay', 'it': 'Italy', 'ee': 'Estonia',
             'cz': 'Czech Republic', 'gf': 'French Guiana', 'cn': 'China', 'kr': 'Korea, Republic of', 'ie': 'Ireland',
             'rs': 'Serbia', 'kh': 'Cambodia', 'bd': 'Bangladesh', 'bn': 'Brunei Darussalam', 'lu': 'Luxembourg',
             'au': 'Australia', 'cr': 'Costa Rica', 'la': "Lao People's Democratic Republic", 'gr': 'Greece',
             'gw': 'Guinea-Bissau', 'eg': 'Egypt', 'yt': 'Mayotte', 'lr': 'Liberia', 'mc': 'Monaco', 'za': 'South Africa',
             'tm': 'Turkmenistan', 'us': 'United States', 'bg': 'Bulgaria', 'bo': 'Bolivia, Plurinational State of',
             'hr': 'Croatia', 'dk': 'Denmark', 'lv': 'Latvia', 'ad': 'Andorra', 'al': 'Albania', 'ch': 'Switzerland',
             'az': 'Azerbaijan', 'zm': 'Zambia', 'sa': 'Saudi Arabia', 'cu': 'Cuba', 'sr': 'Suriname', 'pt': 'Portugal',
             'lb': 'Lebanon', 'jo': 'Jordan', 'er': 'Eritrea', 'mu': 'Mauritius', 'bj': 'Benin', 'tr': 'Turkey', 'gn': 'Guinea',
             'mm': 'Myanmar', 'lk': 'Sri Lanka', 'is': 'Iceland', 'mo': 'Macao', 'nl': 'Netherlands', 'tl': 'Timor-Leste',
             'ne': 'Niger', 'bt': 'Bhutan', 'gy': 'Guyana', 'at': 'Austria', 'sy': 'Syrian Arab Republic', 'cf': 'Central African Republic',
             'zw': 'Zimbabwe', 'gl': 'Greenland', 'fi': 'Finland', 'sl': 'Sierra Leone', 'kw': 'Kuwait', 'hn': 'Honduras',
             'st': 'Sao Tome and Principe', 'mv': 'Maldives', 'dz': 'Algeria', 'sv': 'El Salvador', 'bz': 'Belize', 'pk': 'Pakistan',
             'ru': 'Russian Federation', 'sm': 'San Marino', 'gm': 'Gambia', 'mg': 'Madagascar'}


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None



