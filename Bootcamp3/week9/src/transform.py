def identify_and_remove_duplicate_data(df):
    """Method that removes identifies and removes duplicates"""

    if df.duplicated().sum() > 0:
        df_cleaned = df.drop_duplicates(keep='first')

        print("-" * 50)
        print("Shape of data before removing duplicates:", df.shape)
        print("Shape of data after removing duplicates:", df_cleaned.shape)
        print("-" * 50)

    else:
        print("no duplicates values found")
        df_cleaned = df.copy()

    return df_cleaned
