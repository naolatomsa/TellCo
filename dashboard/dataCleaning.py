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
    data.loc[:, 'TCP DL Retrans. Vol (Bytes)'] = data['Avg RTT UL (ms)'].fillna(data['Avg RTT UL (ms)'].median())
    data.loc[:, 'TCP UL Retrans. Vol (Bytes)'] = data['Avg RTT DL (ms)'].fillna(data['Avg RTT DL (ms)'].median())
    return data

def identify_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return data[(data[column] < lower_bound) | (data[column] > upper_bound)]

# Cap and floor outliers for all numeric columns
def cap_outliers(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data[column] = data[column].clip(lower=lower_bound, upper=upper_bound)
    return data

