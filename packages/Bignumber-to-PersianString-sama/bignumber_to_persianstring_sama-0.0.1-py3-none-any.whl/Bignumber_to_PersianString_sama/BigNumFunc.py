# this code converts a big number into words (with functions)

# region dicts
yekan = {"1": "يک", "2": "دو", "3": "سه", "4": "چهار", "5": "پنج",
         "6": "شش", "7": "هفت", "8": "هشت", "9": "نه", "10": "ده",
         "11": "یازده", "12": "دوازده", "13": "سیزده", "14": "چهارده", "15": "پانزده",
         "16": "شانزده", "17": "هفده", "18": "هجده", "19": "نوزده"}

dahgan = {"2": "بیست", "3": "سی", "4": "چهل", "5": "پنجاه",
          "6": "شصت", "7": "هفتاد", "8": "هشتاد", "9": "نود"}

sadgan = {"1": "یکصد", "2": "دویست", "3": "سیصد", "4": "چهارصد",
          "5": "پانصد", "6": "ششصد", "7": "هفتصد", "8": "هشتصد", "9": "نهصد"}

pasvand = {"1": "", "2": "هزار", "3": "میلیون", "4": "میلیارد", "5": "بیلیارد", "6": "تریلیون", "7": "تریلیارد",
           "8": "کوآدریلیون", "9": "کادریلیارد", "10": "کوینتیلیون", "11": "کوانتینیارد", "12": "سکستیلیون",
           "13": "سکستیلیارد", "14": "سپتیلیون", "15": "سپتیلیارد", "16": "اکتیلیون", "17": "اکتیلیارد",
           "18": "نانیلیون", "19": "نانیلیارد", "20": "دسیلیون", "21": "دسیلیارد", "22": "آندسیلیون",
           "23": "آندسیلیارد", "24": "دودسیلیون", "25": "دودسیلیارد", "26": "تریدسیلیون", "27": "تریدسیلیارد",
           "28": "کوادردسیلیون", "29": "کوادردسیلیارد", "30": "کویندسیلیون", "31": "کویندسیلیارد",
           "32": "سیدسیلیون", "33": "سیدسیلیارد", "34": "گوگول"}
# endregion



final_str = list()  # The result will be saved in this List

# function for building initial List
def find_digits(num):
    res = [num[i-3:i].zfill(3) if i > 2 else num[0:i].zfill(3)
       for i in range(len(num), 0, -3)]  # Splits the input number into 3 digit parts and put them in a List
    res.reverse()   # Reverse the List in order to match with the input number
    return (res)

# function calculation
def calc(res):
    for index, item in enumerate(res):

        # region 1 or 2 digits part

        if int(item[0]) == 0:
            if int(item[1]) == 0:
                if int(item[2]) == 0:
                    if len(res) == 1:  # 000
                        print("صفر")
                    continue
                final_str.append(yekan.get(item[2]))    # 00X

            elif int(item[1]) == 1:  # 01X
                final_str.append(yekan.get(item[1:3]))

            elif int(item[1]) in range(2, 10):
                if int(item[2]) == 0:  # 0X0
                    final_str.append(dahgan.get(item[1]))

                else:  # 0XX
                    final_str.append(dahgan.get(
                        item[1]) + " و " + yekan.get(item[2]))

        # endregion

        # region 3 digits part

        else:
            if int(item[1]) == 0:
                if int(item[2]) == 0:   # X00
                    final_str.append(sadgan.get(item[0]))

                else:  # X0X
                    final_str.append(sadgan.get(
                        item[0]) + " و " + yekan.get(item[2]))

            elif int(item[1]) == 1:  # X1X
                final_str.append(sadgan.get(
                    item[0]) + " و " + yekan.get(item[1:3]))

            elif int(item[1]) in range(2, 10):
                if int(item[2]) == 0:  # XX0
                    final_str.append(sadgan.get(
                        item[0]) + " و " + dahgan.get(item[1]))

                else:  # X X X
                    final_str.append(sadgan.get(
                        item[0]) + " و " + dahgan.get(item[1]) + " و " + yekan.get(item[2]))
        # endregion

        final_str[len(final_str)-1] += " " + \
            pasvand.get(str(len(res)-index))
                        # Creats a List of 3-digit parts in words plus their suffixes
   
    return final_str

def convert_func(num):
    result = " و ".join(calc(find_digits(num)))  # Adds connector " و " to the final string
    print (result)
    return result # Prints final result


