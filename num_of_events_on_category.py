import pandas as pd
import csv 


def getting_windows_event_details(new_list): # defining the function
    starting_and_ending_timings_list = []

    for each_row in new_list: # iterating each row from the passing list as argument
        
        row_1 = new_list[0]
        if len(row_1) != 0:
            date_and_time = row_1[0]
            source = row_1[1]
            event_id = row_1[2]
            event_type = row_1[3]
        
            count = 0
            index_list = []
            word = ""
            for i in range(len(new_list)): # here also iterating each row for comparison
                
                row_2 = new_list[i]
                if len(row_2) != 0:
                    date_and_time_of_row_2 = row_2[0]
                    source_of_row_2 = row_2[1]
                    event_id_of_row_2 = row_2[2]
                    event_type_of_row_2 = row_2[3]
                    
                    condintion_1 = (source == source_of_row_2)
                    condintion_2 = (event_id == event_id_of_row_2)
                    
                    if condintion_1 and condintion_2:
                        
                        count += 1
                        index_list.append(i)
                        word = source_of_row_2

                    elif count > 1:
                        break 
        
                
            # print(row_1)        
            
            if len(index_list) > 1: # appending the logging timings only on there are two loggings
                starting_time = new_list[index_list[0]][0]
                ending_time = new_list[index_list[-1]][0]
                source_event = new_list[index_list[0]][1]
                task_category = new_list[index_list[0]][3]
                
                starting_and_ending_timings_list.append([starting_time, ending_time, source_event, task_category])
                
        
            for j in range(len(index_list)): # only deleting the comparions done rows based on indices
                for index in range(len(new_list)): # accessing indices of rows of list
                    row = new_list[index]
                    
                    if len(row) != 0:
                        if row[1] == word:
                            
                            del new_list[index] # deleting the row item from the list after getting the logging data
                            break
                        
                    
    
            index_list = [] # again updating the index_list as empty
            count = 0 # also count updating to 0 after completing the loop
        
    return starting_and_ending_timings_list 



def load_data(file_name): # defining function to get data from the CSV file
    data_list = []
    with open(file_name) as detials:
        csv_data = csv.reader(detials, delimiter=",") 
        next(csv_data)
        for row in csv_data:
            data_list.append(row[1:-1]) # accessing required columns
            
    return data_list 

my_list = load_data("CyberSophy.csv") # calling the load data function

my_list = my_list[::-1] # ascending order of my_list

starting_and_ending_timings_list = getting_windows_event_details(my_list) # calling getting_windows_event_details function


task_category_list = []

    
for each_event_detail in starting_and_ending_timings_list:
    
    task_category = each_event_detail[-1]
    if task_category not in task_category_list:
        task_category_list.append(task_category)
        
        
print(task_category_list)

task_category_dict = {}
num_of_task_categories_list = []

for task in task_category_list:
    counter = 0
    for event_detail in starting_and_ending_timings_list:
        task_category = event_detail[-1]
        if task_category == task:
            counter += 1 
        
    task_category_dict[task] = [counter]
    num_of_task_categories_list.append(counter)
    counter = 0

df = pd.DataFrame(task_category_dict, columns=task_category_list)

df.to_csv("D:\\num-of-events-on-category.csv")

df = pd.read_csv("D:\\num-of-events-on-category.csv")


print(task_category_dict)
print(num_of_task_categories_list)

print(df)




            
    