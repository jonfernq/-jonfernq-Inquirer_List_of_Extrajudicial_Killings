
Philippine War on Drugs (2016-17): 
Extrajudicial Killings from June, 2016 to February, 2017 

Dataset of extrajudicial killings during the first eight months of the war on drugs from the Inquirer newspaper's 
curated list. Detailed documentation in data-cleaning script:

kill_list_make_dataset.py: analyze the data in the Inquirer's 'Kill List' for the extrajudicial killings  

DATA
kill_list.csv: clean dataset
kill_list.txt: raw unclean data from newspaper list
kill_list_article_with_link.txt: original newspaper article source of data with url

date_typos.txt: data entered incorrectly with typos (corrected manually in kill_list.txt
kill_list_nodate_notime.txt: data missing a date and time with only an indication of a range of dates during which it occured (to be added during feature engineering stage of analysis)  
not_extrajudicial_killing.txt: data that is clearly not an extrajudicial according to the description given (deleted manually) 
wrong_field_count.txt:  records that do not have the right number of fields for various reasons (corrected manually) 

For further information on datasets in this area and extrajudicial killing in the war on drugs, see:

Fernquest, Jon. Extrajudicial Killing and the State in the Philippines: An Epidemiology of Violence [Unpublished manuscript] https://www.academia.edu/44501291/Extrajudicial_Killing_and_the_State_in_the_Philippines_An_Epidemiology_of_Violence

Fernquest, J. (2018). “State killing, Denial and Cycles of Violence in the Philippines.” Philippine
Sociological Review (Special Issue on Sociology of Justice), Volume 66. Retrieved on 6/22/2020 from:
https://www.jstor.org/stable/e26905839
https://www.academia.edu/40715917/State_Killing_Denial_and_Cycles_of_Violence_in_the_Philippines

Johnson, David and Jon Fernquest. 2018. “Governing through Killing: The War on Drugs in the
Philippines.” Asian Journal of Law and Society 5(2):359–390.
https://www.academia.edu/40715870/Governing_through_Killing_The_War_on_Drugs_in_the_Philippines






