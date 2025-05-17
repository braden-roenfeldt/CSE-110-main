#12 team activity
#Hansen, Kristi 9am
#Braden Roenfeldt
sizecomp = 0
old_total = 0
new_total = 0
bom_total = 0
pogp_total = 0
dnc_total  = 0
with open("books_and_chapters.txt") as books:
    for line in books:
        line = line.strip()
        line_list = line.split(":")
        book_name = line_list[0]
        chapters = int(line_list[1])
        location = line_list[2]
        print(f"{location}, Book: {book_name}, Chapters: {chapters}.\n")
        if sizecomp <= chapters:
            sizecomp = chapters     #finds the largest chapter and what book it is
            largest_book = book_name
        if location == "Old Testament":
            old_total += chapters
        elif location == "New Testament":
            new_total += chapters
        elif location == "Book of Mormon":
            bom_total += chapters
        elif location == "Pearl of Great Price":
            pogp_total += chapters
        elif location == "Doctrine and Covenants":
            dnc_total += chapters
chapter_list = [old_total, new_total, bom_total, pogp_total, dnc_total]
chapter_list.sort()
print(f"The Book with the most chapters is the ")