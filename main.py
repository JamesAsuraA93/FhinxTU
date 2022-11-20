
def read_file_clean_data(raw_list_data):

    temp_lst = []
    rows_number = len(raw_list_data) # จำนวนแถวทั้งหมด
    for index_row in range(rows_number):
        if index_row != 0:
            # print(raw_list_data[index_row].strip().split(","))
            list_each_row = raw_list_data[index_row].strip().split(",")
            h = eval(list_each_row[2])
            w = eval(list_each_row[3])
            BMI = float(f'{(w / (h ** 2)):.2f}')
            # print(f"{list_each_row[1]}'s BMI = {BMI}")
            temp_lst.append([list_each_row[1],BMI])

    # print(temp_lst)
    return temp_lst
    # print('avg', sum(temp_lst)/len(temp_lst))


def AVG_Process(data):
    # sample data [['JamesA', 22.77], ['JamesB', 9.52], ['JamesC', 24.61], ['JamesD', 25.47], ['JamesE', 28.93],
    Sum = 0
    for item in data:
        Sum += float(item[1])
        # print(item)
    return Sum / len(data)

def write_file(data,filename):
    # sample data [['JamesA', 22.77], ['JamesB', 9.52], ['JamesC', 24.61], ['JamesD', 25.47], ['JamesE', 28.93],
    # ['JamesF', 24.34], ['JamesG', 16.94]]
    file_in = open(filename,'w')
    # print(data)
    temp_data = []
    for item in data:
        # item = row ที่จะเขียน
        temp_data.append(f'{item[0]},{item[1]}\n')
        # print(item)
    # print(temp_data)
    file_in.writelines(temp_data)
    file_in.close()
    return


def append_file(data,filename):

    file_in = open(filename, 'a')
    file_in.write(data)
    file_in.close()
    return

# BMI = Kg / m^2

fileNormal = open('data','r')
fileCSV = open('dataCSV.csv','r')

data = fileNormal.readlines()

write_file(read_file_clean_data(data),'temptest.txt')

avg = AVG_Process(read_file_clean_data(data))

append_file(f'AVG BMI All LIst =  {avg}','data')

# print(fileNormal.readlines())
# print(fileCSV.readlines())

fileCSV.close()
fileNormal.close()
