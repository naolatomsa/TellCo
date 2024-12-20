def missing_percentage(data, thresholds):
    missing_percentage = (data.isnull().sum() / len(data)) * 100
    if thresholds != 0 & thresholds!=57 & thresholds!=53:
        missing_columns_percentage = missing_percentage[missing_percentage < thresholds]
        return missing_columns_percentage;
    else:
        missing_columns_percentage = missing_percentage[missing_percentage > thresholds]
        return missing_columns_percentage;


def drop_row(data):
    data = data.dropna(subset=['Last Location Name',
    'DL TP < 50 Kbps (%)',
    '50 Kbps < DL TP < 250 Kbps (%)',
    '250 Kbps < DL TP < 1 Mbps (%)',
    'DL TP > 1 Mbps (%)',
    'UL TP < 10 Kbps (%)',
    '10 Kbps < UL TP < 50 Kbps (%)',
    '50 Kbps < UL TP < 300 Kbps (%)',
    'UL TP > 300 Kbps (%)',
    'Nb of sec with Vol DL < 6250B',
    'Nb of sec with Vol UL < 1250B'])
    return data;


def fill_missing_values(data):
    data.loc[:, 'Avg RTT UL (ms)'] = data['Avg RTT UL (ms)'].fillna(data['Avg RTT UL (ms)'].median())
    data.loc[:, 'Avg RTT DL (ms)'] = data['Avg RTT DL (ms)'].fillna(data['Avg RTT DL (ms)'].median())
    return data