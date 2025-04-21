compress_input = input("Enter the tet you want to compress: ")
mode = False
done = False
compress_file_text = ""

mode_input = input("Choose mode: ")

current_text = compress_input

#compress_input = "aaaa111bbbccaaa\\\\\\\\\\\\\\\\\\\\     ,,,,"
#decompress_input = "a411b3c2a3"
#decompress_text_input = "a4,13,b3,c2,a3,\\10, 5,,10"

def compress_text_string(s: str) -> str:
    if not s:
        return ""
    else:
        comp = ""
        comp_text = ""
        current_letter = ''
        counter = 1
        for i in range(len(s)):
            if current_letter == s[i]:
                counter += 1
                if i == len(s) - 1:
                    comp = comp + current_letter + str(counter)
                    comp_text =comp_text + current_letter + str(counter)
            else:
                if i != 0:
                    comp = comp + current_letter + str(counter)
                    comp_text =comp_text + current_letter + str(counter) + ","
                current_letter = s[i]
                counter = 1
        return comp_text
    
def compress_string(s: str) -> str:
    st = compress_text_string(s)
    comp = ''
    while st.find(",") != -1:
            if st[0] == ",":
                if st[1:].find(",") != -1:
                    comma_index = st[1:].find(",")
                    comp = comp + st[0:comma_index]
                    st = st[(comma_index + 1):]
                else:
                    comp = comp = comp + st[0:comma_index]
                    return comp
            else:
                comma_index = st.find(",")
                comp = comp = comp + st[0:comma_index]
                st = st[(comma_index + 1):]
    return comp
    
def decompress_string(s: str) -> str:
    if not s:
        return ""
    else:
        decomp = ""
        copied_letter = ''
        counter = 0
        while s.find(",") != -1:
            if s[0] == ",":
                if s[1:].find(",") != -1:
                    comma_index = s[1:].find(",")
                    block = s[0:comma_index]
                    copied_letter = block[0]
                    counter = block[1:]
                    decomp = decomp + (copied_letter * int(counter))
                    s = s[(comma_index + 1):]
                else:
                    decomp = decomp + (s[0] * int(s[1:]))
                    return decomp
            else:
                comma_index = s.find(",")
                block = s[0:comma_index]
                copied_letter = block[0]
                counter = block[1:]
                decomp = decomp + (copied_letter * int(counter))
                s = s[(comma_index + 1):]
        decomp = decomp + (s[0] * int(s[1:]))
        return decomp

while done == False:
    if(mode_input == "compress" or mode_input == "c"):
        if(mode == True):
            print("Already compressed")
        else:
            print(compress_string(current_text))
            compress_file_text = compress_text_string(current_text)
            f = open("compress.txt", "w")
            f.write(compress_file_text)
            f.close()
            mode = True
    if(mode_input == "decompress" or mode_input == "dc"):
        if(mode == False):
            print("Already decompressed")
        else:
            print(decompress_string(compress_file_text))
            f = open("compress.txt", "r")
            print(f.read())
            mode = False
            compress_file_text = ""
    mode_input = input("Choose next mode: ")
    if mode_input == "done" or mode_input == "d":
        done = True