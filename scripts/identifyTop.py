def top(data, col, value):
    top = data[col].value_counts().head(value)
    return top;

#Next, identify the top 5 handsets per top 3 handset manufacturer
def top_3_handset_per_top_5_manufacturer(data):
    #  Top 5 Handsets per Top 3 Manufacturers
    top_3_manufacturers = data['Handset Manufacturer'].value_counts().head(3)
    top_5_per_manufacturer = {}
    for manufacturer in top_3_manufacturers.index:
        top_5_per_manufacturer[manufacturer] = data[data['Handset Manufacturer'] == manufacturer]['Handset Type'].value_counts().head(5)
        return top_5_per_manufacturer;