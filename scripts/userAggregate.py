import pandas as pd
def user_aggregate(data):
    user_aggregated = data.groupby('IMSI').agg({
        'Bearer Id': 'count',  # Number of xDR sessions
        'Dur. (ms)': 'sum',  # Total session duration
        'Total DL (Bytes)': 'sum',  # Total download volume
        'Total UL (Bytes)': 'sum',  # Total upload volume
        'Social Media DL (Bytes)': 'sum',
        'Social Media UL (Bytes)': 'sum',
        'Google DL (Bytes)': 'sum',
        'Google UL (Bytes)': 'sum',
        'Email DL (Bytes)': 'sum',
        'Email UL (Bytes)': 'sum',
        'Youtube DL (Bytes)': 'sum',
        'Youtube UL (Bytes)': 'sum',
        'Netflix DL (Bytes)': 'sum',
        'Netflix UL (Bytes)': 'sum',
        'Gaming DL (Bytes)': 'sum',
        'Gaming UL (Bytes)': 'sum',
        'Other DL (Bytes)': 'sum',
        'Other UL (Bytes)': 'sum',
    }).reset_index()
    return user_aggregated

def calculate_total_data_volume(data):
    user_aggregated = user_aggregate(data)
    # Calculate Total Data Volume (DL + UL)
    user_aggregated['Total Data Volume'] = user_aggregated['Total DL (Bytes)'] + user_aggregated['Total UL (Bytes)']

    # Calculate Total Data Volume for Social Media
    user_aggregated['Social Media'] = user_aggregated['Social Media DL (Bytes)'] + user_aggregated['Social Media UL (Bytes)']

    # Calculate Total Data Volume for Google
    user_aggregated['Google'] = user_aggregated['Google DL (Bytes)'] + user_aggregated['Google UL (Bytes)']

    # Calculate Total Data Volume for Email
    user_aggregated['Email'] = user_aggregated['Email DL (Bytes)'] + user_aggregated['Email UL (Bytes)']

    # Calculate Total Data Volume for YouTube
    user_aggregated['YouTube'] = user_aggregated['Youtube DL (Bytes)'] + user_aggregated['Youtube UL (Bytes)']

    # Calculate Total Data Volume for Netflix
    user_aggregated['Netflix'] = user_aggregated['Netflix DL (Bytes)'] + user_aggregated['Netflix UL (Bytes)']

    # Calculate Total Data Volume for Gaming
    user_aggregated['Gaming'] = user_aggregated['Gaming DL (Bytes)'] + user_aggregated['Gaming UL (Bytes)']

    # Calculate Total Data Volume for Other Applications
    user_aggregated['Other'] = user_aggregated['Other DL (Bytes)'] + user_aggregated['Other UL (Bytes)']
    return user_aggregated;

def segment_user(data):
    user_aggregated = calculate_total_data_volume(data)
    user_aggregated['Usage Category'] = pd.qcut(
    user_aggregated['Total Data Volume'], 
    q=[0, 0.25, 0.75, 1], 
    labels=['Light', 'Moderate', 'Heavy']
    )
    return user_aggregated;