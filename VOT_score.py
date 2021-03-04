import sys

TEXT_ERROR = "TEXT_ERROR"

def main():    
    textgrid_filename = sys.argv[1]
    
    textgrid_file = open(textgrid_filename, "r")    
    textgrid_file_lines = textgrid_file.readlines()
    textgrid_file.close()
    
    interval_2_xmin = float(textgrid_file_lines[19].split()[-1])
    interval_2_xmax = float(textgrid_file_lines[20].split()[-1])
    interval_2_text = textgrid_file_lines[21].split("\"")[-2]
    
    VOT_score = interval_2_xmax-interval_2_xmin
    if (interval_2_text == ""):
        print(VOT_score)
    elif (interval_2_text == "-"):
        print((-1)*VOT_score)    
    else:
        print(TEXT_ERROR)
    
main()