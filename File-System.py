# Mengchen Xu, ID: 61281584 ICS 32 project1

from pathlib import Path
from pathlib import *
import shutil

# find all files that is under the input directory
def handle_input_D(dire_path:Path)->list:
    '''this is the function to handle command D'''
    result_file = []
    all_p = list(dire_path.iterdir())
    for path in sorted(all_p):
        if path.is_file():
            result_file.append(path)
    return result_file
                    
# find all files that is under the input directory as well as all files under subdirectories
def handle_input_R(dire_path:Path)->list:
    '''this is the function to handle command R'''
    result_file = []
    for dirc in sorted(dire_path.iterdir()):
        if dirc.is_file():
            result_file.append(dirc)
    for dirc in sorted(dire_path.iterdir()):
        if dirc.is_dir():
            result_file.extend(handle_input_R(dirc)) # the recursion step for input R
    return result_file
                               

#first stage: handle input of D and R
def input_d_r():
    done = False
    while not done:
        user_input = input()
        a = user_input.split(' ', 1)
        letter = a[0]
        dir_path = Path(a[-1])
        if dir_path.exists():

            if letter == "D":
                d_list = handle_input_D(dir_path)
                for path in d_list:
                    print(path)
                return d_list
                done = True

            elif letter == "R":
                r_list = handle_input_R(dir_path)
                for f_path in r_list:
                    print(f_path)
                return r_list
                done = True
            else:
                print("ERROR")
                done = False
        else:
            print("ERROR")
            done = False


# find out all the path of files that has the same name after the input N
def handle_input_N(result_list,file_name)->list:
    '''handle the input N'''
    collect_list = []
    for path in result_list:
        n = PurePosixPath(path).name
        if n == file_name:
            collect_list.append(path)
    return collect_list
            
# find out all the path of files that has the same extension after the input E
def handle_input_E(result_list,extension)->list:
    '''handle the input E'''
    collect_list = []
    if "." not in extension:
        extension = "." + extension
    for path in result_list:
        e = PurePosixPath(path).suffix
        if e == extension:
            collect_list.append(path)
    return collect_list

# find out all the path of text files that include the words after the input T
def handle_input_T(result_list:list,words:str)->list:
    '''determine if a path is a text or not a text'''
    path_list = []
    for path in result_list:
        try:                                # determine whether a file is text file
            text = open(path,'r')
            textlist = text.readlines()
            for items in textlist:
                if words in items:
                    path_list.append(path)
        except OSError:
            pass
            
        except ValueError:
            pass
        finally:
            text.close()
    return path_list

# find out all path of files that has size less than the number after the input <
def handle_input_less(result_list:list,byte:str)->list:
    '''handle the input <'''
    collect_list = []
    for path in result_list:
        size = path.stat().st_size                     
        if size < int(byte):
            collect_list.append(path)
    return collect_list
            
# find out all path of files that has size greater than the number after the input > 
def handle_input_more(result_list:list,byte:str)->list:
    '''handle the input <'''
    collect_list = []
    for path in result_list:
        size = path.stat().st_size
        if size > int(byte):
            collect_list.append(path)
    return collect_list


# the second stage: handle input of: A,N,E,T,<,>                                                                                                                                                                                                        
def input_handle(prefound_list):
    done = False
    while not done:
        user_input = input()
        a = user_input.split(' ', 1)
        letter = a[0]
        message = a[-1]

        if letter == "A":
            for path in prefound_list:
                print(path)
            return prefound_list
            done = True

        elif letter == "N" and len(message) != 0:
            n_list = handle_input_N(prefound_list,message)
            if len(n_list) == 0:
                print("ERROR")
                done = False
            else:
                for path in n_list:
                    print(path)
                return n_list
                done = True

        elif letter == "E" and len(message) != 0:
            e_list = handle_input_E(prefound_list,message)
            if len(e_list) == 0:
                print("ERROR")
                done = False
            else:
                for path in e_list:
                    print(path)
                return e_list
                done = True

        elif letter == "T" and len(message) != 0:
            t_list = handle_input_T(prefound_list,message)
            if len(t_list) == 0:
                print("Error")
            else:
                for path in t_list:
                    print(path)
                return t_list
                done = True
     
        elif letter == "<" and len(message) != 0:
            less_list = handle_input_less(result_list,message)
            if len(less_list) == 0:
                print("ERROR")
            else:
                for path in less_list:
                    print(path)
                return less_list

        elif letter == ">" and len(message) != 0:
            more_list = handle_input_more(result_list,message)
            if len(more_list) == 0:
                print("ERROR")
            else:
                for path in more_list:
                    print(path)
                return more_list
        else:
            print("ERROR")
            done = False
    
       
# make duplicate copies of files that in the list      
def handle_input_D2(prefound_list:list)->None:
    '''handle the input D'''
    for path in prefound_list:
        duplicate_path = str(path) + '.dup'
        try:
            shutil.copy(path,duplicate_path)
        except:
            pass
        
# the third stage handle input of F,D,T
def handle_input_f_d_t(result_list2:list):
    '''handle the input f,d,t and make some actions on them'''
    done = False
    while not done:
        user_input = input()
        if user_input == "F":
            for path in result_list2:
                if path == "":
                    None                 
                try:                               # determine whether a file is text file
                    file = open(path,'r')
                    first_line = file.readline()
                    print(first_line.strip())
                    
                except OSError:
                    print('NOT TEXT')
                except ValueError:
                    print('NOT TEXT')
                    pass
                finally:
                    done = True
            
        elif user_input == "D":
                handle_input_D2(result_list2)
                done = True
            
        elif user_input == "T":
            for path in result_list2:
                path.touch()                                        
                done = True
        else:
            print("ERROR")
            done = False
           
result_list = input_d_r()
second_result_list = input_handle(result_list)     
handle_input_f_d_t(second_result_list)
