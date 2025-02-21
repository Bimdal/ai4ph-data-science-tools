#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd

# Load the Covid Datast CSV file
file_path = "C:/Users/bimda/Downloads/conposcovidloc (1).csv"  
Covid_Cases = pd.read_csv(file_path)


# Display the first few rows
print(Covid_Cases.head())


# In[18]:


# Total number of rows in covid data set
num_rows = Covid_Cases.shape[0]

print(f"Total number of rows in the dataset: {num_rows}")


# In[9]:


import pandas as pd

# Load the dataset
file_path = "C:/Users/bimda/Downloads/conposcovidloc (1).csv"  
df = pd.read_csv(file_path)

# List all column names
columns = df.columns.tolist()
print("Columns in the dataset:")
print(columns)

# Total number of rows
total_rows = df.shape[0]
print(f"\nTotal number of rows: {total_rows}")


# In[19]:


# Summary statistics for numerical columns
print("\nNumerical Data Summary:")
print(Covid_Cases.describe())


# In[31]:


import pandas as pd

# Define the file path
file_path = r"C:/Users/bimda/Downloads/conposcovidloc (1).csv"

# Load the CSV file into a DataFrame
Covid_cases = pd.read_csv(file_path)

# Rename the column
Covid_cases.rename(columns={"Outcome1": "Outcome"}, inplace=True)

# Replace empty rows (NaN values) with "SURVIVED"
Covid_cases["Outcome"].fillna("SURVIVED", inplace=True)

# Display the first few rows to verify
print(Covid_cases.head())

# Save the cleaned dataset (optional)
df.to_csv(r"C:/Users/bimda/Downloads/conposcovidloc_cleaned.csv", index=False)


# In[32]:


# Count occurrences of each category
outcome_counts = Covid_cases["Outcome"].value_counts()

# Display the counts
print(outcome_counts)


# In[35]:



# List of columns to drop
columns_to_drop = [
    'Reporting_PHU_Postal_Code',
    'Reporting_PHU_Website',
    'Reporting_PHU_Latitude',
    'Reporting_PHU_Longitude',
    'Reporting_PHU_Address',
    'Reporting_PHU_City',
    'Reporting_PHU_ID'
]

# Drop the specified columns
Covid_cases.drop(columns=columns_to_drop, inplace=True, errors='ignore')

# Display the first few rows to verify
print(df.head())


# In[37]:


# Count occurrences of each age
age_counts = df["Age_Group"].value_counts().sort_index()

# Display the counts
print(age_counts)


# In[44]:


# Count the occurrences of each age group and normalize to get proportions
age_group_proportion = Covid_cases["Age_Group"].value_counts(normalize=True)

# Display the result
print(age_group_proportion.to_frame())


# In[49]:


# Plot the proportions
plt.figure(figsize=(8, 5))
age_group_proportion.sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel("Age Group")
plt.ylabel("Proportion")
plt.title("Proportion of Each Age_Group")
# Show the plot
plt.show()


# In[50]:


# Countplot for Gender distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Client_Gender', data=df, palette='coolwarm')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[51]:


# Group by Age Group, Client Gender, and Outcome to get proportions
age_gender_outcome_proportion = df.groupby(["Age_Group", "Client_Gender"])["Outcome"].value_counts(normalize=True) 

# Display results
print(age_gender_outcome_proportion)


# In[55]:


# filter rows where Outcome is 'FATAL'

if "Outcome" in df.columns:
    fatal_cases = df[df["Outcome"] == "FATAL"]
    print(fatal_cases) 
    
    # Display filtered dataset
else:
    print("The column 'Outcome' does not exist in the dataset.")


# In[71]:




# Ensure "Outcome" column exists before filtering
if "Outcome" in df.columns:
    # Filter rows where Outcome is 'FATAL'
    fatal_cases = df[df["Outcome"] == "FATAL"]

    # Normalize fatal cases based on Age Group
    fatal_cases_normalized = fatal_cases["Age_Group"].value_counts(normalize=True) 

    # Display the normalized fatal cases
    print(fatal_cases_normalized.to_frame())  
    

    # Plot a doughnut chart
    plt.figure(figsize=(8, 8))
    plt.pie(fatal_cases_normalized, labels=fatal_cases_normalized.index, autopct='%1.1f%%', 
            startangle=90, pctdistance=0.85, wedgeprops={'edgecolor': 'black'})

    # Draw a white circle at the center to make it look like a doughnut chart
    center_circle = plt.Circle((0, 0), 0.70, fc='white')
    plt.gca().add_artist(center_circle)

    plt.title("Normalized Distribution of Fatal Cases by Age Group")
    plt.show()

else:
    print("The column 'Outcome' does not exist in the dataset.")



    


# In[74]:


# Convert date columns to datetime format
date_columns = ['Case_Reported_Date', 'Specimen_Date', 'Test_Reported_Date']
for col in date_columns:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# Calculate Test Turnaround Time
if "Test_Reported_Date" in df.columns and "Specimen_Date" in df.columns:
    df['Test_Turn_Around'] = (df['Test_Reported_Date'] - df['Specimen_Date']).dt.days

    # Generate descriptive statistics
    test_turnaround_summary = df['Test_Turn_Around'].describe()
    
     # Generate descriptive statistics with specific percentiles
    percentiles = [0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
    test_turnaround_summary = df['Test_Turn_Around'].describe(percentiles=percentiles)

    # Display the summary
    print(test_turnaround_summary)


    # Display the summary
    print(test_turnaround_summary)

else:
    print("One or more required columns (Specimen_Date, Test_Reported_Date) are missing in the dataset.")


# In[77]:



    # Filter cases where Test Turnaround Time is negative
    negative_turnaround_cases = df.loc[df['Test_Turn_Around'] < 0]

    # Display first 5 rows
    print(negative_turnaround_cases.head())


# In[80]:


# Calculate Test Turnaround Time
if "Test_Reported_Date" in df.columns and "Specimen_Date" in df.columns:
    df['Test_Turn_Around'] = (df['Test_Reported_Date'] - df['Specimen_Date']).dt.days

    # Generate descriptive statistics
    test_turnaround_summary = df['Test_Turn_Around'].describe()

    # Display the summary
    print(test_turnaround_summary)


# In[86]:


# Calculate Test Turnaround Time
if "Test_Reported_Date" in df.columns and "Specimen_Date" in df.columns:
    df['Test_Turn_Around'] = (df['Test_Reported_Date'] - df['Specimen_Date']).dt.days

    # Drop rows where Test Turnaround Time is greater than 14 days
    df.drop(df[df['Test_Turn_Around'] > 14].index, inplace=True)

    # Generate descriptive statistics after removing high outliers
    test_turnaround_summary = df['Test_Turn_Around'].describe()

    # Display the updated summary statistics
    print(test_turnaround_summary)
    
    # Plot histogram of Test Turnaround Time
    df['Test_Turn_Around'].dropna().hist(bins=15, color='skyblue', edgecolor='black', alpha=0.7, figsize=(8, 5))

    plt.xlabel("Test Turnaround Time (days)")
    plt.ylabel("Frequency")
    plt.title("Distribution of Test Turnaround Time")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the histogram
    plt.show()


# In[88]:


# Extract Year and Month from Case_Reported_Date
if "Case_Reported_Date" in df.columns:
    df['Case_Reported_Year'] = df['Case_Reported_Date'].dt.year
    df['Case_Reported_Month'] = df['Case_Reported_Date'].dt.month

    # Display the first few rows to confirm the new columns
    print(df.head())


# In[94]:


# Group by Year and Month, then calculate the mean Test Turnaround Time
if "Case_Reported_Year" in df.columns and "Case_Reported_Month" in df.columns and "Test_Turn_Around" in df.columns:
    mean_turnaround = df.groupby(["Case_Reported_Year", "Case_Reported_Month"])["Test_Turn_Around"].mean()

    # Display the grouped mean Test Turnaround Time
    print(mean_turnaround.to_frame())
    
    # Plot the mean Test Turnaround Time over time
    plt.figure(figsize=(10, 5))
    mean_turnaround.plot(marker='o', linestyle='-')
    
    plt.xlabel("Year, Month")
    plt.ylabel("Mean Test Turnaround Time (days)")
    plt.title("Monthly Mean Test Turnaround Time Over the Years")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5)

    # Show the plot
    plt.show()
    
    
    # Plot the daily case counts over time
    plt.figure(figsize=(12, 6))
    case_counts.plot(marker='o', linestyle='-')
    
    plt.xlabel("Case Reported Date")
    plt.ylabel("Number of Cases")
    plt.title("Daily Case Counts Over Time")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.5)

    # Show the plot
    plt.show()


# In[ ]:




