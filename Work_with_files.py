def Write_log (string):
    file = open("Machining_log.txt", 'a')
    file.write(string + '\n')
    file.close()
    return(string)
def Clear_log ():
    file = open("Machining_log.txt", 'w')
    file.close()
