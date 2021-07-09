
# kill_list_make_dataset.py: analyze the data in the Inquirer's 'Kill List' for the extrajudicial killings  

# The list takes the form of lines detailing killings grouped by date in reverse order 
# The columns in original newspaper lines:               TIME, PERSON, LOCATION, CIRCUMSTANCES
# The columns in dataset:                                  SERIAL_NUMBER, DATE, TIME, PERSON, LOCATION, CIRCUMSTANCES

# step #1: make a dataset 

# prior to running python data-cleaning script
# 1. remove killings without specific date and put in separate file
# 2. remove those not actually killed (mistakenly identified as victims)
# 3. remove one killing that is clearly not an extrajudicial killing according to its description
# 4. remove meaningless asterixes at beginning of record

# read kill_list.txt file into list 
# filter out blank lines
# insert dates, which are headers, into killings, which are the lines of the file, or in program logic:   
# if date, then (if new date, then change date), else if killing, then insert date and add to new killing list
# add serial number for each killing that identifies it and provides order in killing list
# write list to csv file

# step #2: feature engineering (make a dataset that machine learning algorithms can use) 
# step #3: do exploratory data analysis (EDS) with visualizations and statistics for the dataset
# For some EDS see: 
# Greene, Travis. 2019. "Visualizing Extra-judicial Killings in the Philippines." Humanistic Data Science
# Feb 18, 2019. Retrieved on 7/3/2021 from: https://greenet09.github.io/datasophy/2019/02/18/ph-killing.html

# READ IN LINES & REMOVE BLANKLINES & CONVERT STRING LINE TO LIST LINE
# from table published in Inquirer Philippine newspaper into list 
infile = 'C:\\A\\KILL_LIST\\kill_list.txt' 
lines = []
with open(infile,'rt',encoding='utf-8') as f: 
    for line in f: 
        lines.append(line.strip())
newlines = []
for line in lines: 
    if line != '':  
        newlines.append(line)
lines = newlines 
newlines = []
for line in lines: 
    l = line.split('|')
    m = [] 
    for i in l:
        m.append(i.strip())
    newlines.append(m)
lines = newlines 
newlines = []

# ADD FIRST FIELD IF MISSING (TIME OF DAY) 
import re
time_regex = re.compile(r'(\d{1,2}\:\d{2}\s+(a\.m|p\.m)(\.)*|Dawn|Early morning|Morning|Afternoon|Evening|Late afternoon|Late evening|Before midnight|Before dawn)')
for line in lines:
    if (len(line) > 1) and (not time_regex.search(line[0])):        # if the first field is not a time of day, then this field is missing and must be added
         newlines.append(['notime'] + line) 
         #print(line)
    else:
         newlines.append(line) 
lines = newlines 
newlines = []

# FIELD COUNT & CHECK 
print('\n LINES WITH INCORRECT FIELD COUNT:')

def get_field_count(lines):
    field_count = [0,0,0,0,0,0,0,0,0,0]
    for line in lines:
        if (len(line) - 1 <= 10): 
            field_count[len(line)-1] = field_count[len(line)-1] + 1 
        else: 
            print('ERROR: len(line) - 1 = ',  len(line) - 1)
    return field_count

print('\nFIELD COUNTS FOR LINES:' + str(get_field_count(lines)) + '\n\n')

# LIST LINES WITH INCORRECT FIELD COUNT (3,5,6), not 4
for line in lines:
    if (len(line) != 4) and (len(line) != 1): 
         print('\nFIELDS: ' + str(len(line)) + ', MISSING: ' + str(4 - len(line)) + ', LINE: ' + str(line))

# DATA VALIDATION FINISHED

# ADD DATE FIELD 
# add date heading in table to beginning of each line that details a killing         
# if date, then (if new date, then change date), else if killing, then insert date and add to new killing list
import re
month_regex = re.compile(r'(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s+\d{1,2}\,\s+\d{4}')
newlines = [] 
curr_date = 'nodate' 
date_line_count = killing_line_count = total_line_count = 0
for line in lines: 
        total_line_count = total_line_count + 1 
        if month_regex.search(line[0]):  # if date 
             curr_date = line[0] 
             date_line_count = date_line_count + 1 
        else:                                            # else is killing, then add date to front 
              newlines.append([curr_date] + line)  
              killing_line_count = killing_line_count + 1
lines = newlines 
newlines = []

print('\nFIELD COUNTS FOR LINES:' + str(get_field_count(lines)) + '\n\n')

# RECORD ID: provide record id that corresponds to the serial order of the killing 
killing_count = len(lines)
for line in lines: 
    line.insert(0, str(killing_count))
    killing_count = killing_count - 1

print('\nFIELD COUNTS FOR LINES:' + str(get_field_count(lines)) + '\n\n')
print(lines)

# write lines to file to check them 
outfile = 'C:\\A\\KILL_LIST\\kill_list_clean.csv' 
with open(outfile,'wt',encoding='utf-8') as f: 
    for line in lines:
        f.write('\t'.join(line) + '\n') 

# END OF PROCESSING


