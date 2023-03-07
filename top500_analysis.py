
import csv


## Want to perform segmentation by column, percentage breakdown for attribute



def analysis_top_firms(file_name):

    firms = 533

    ## 1. STATE SEG
    print('State breakdown')
    print()
    print()
    state_unsort = []
    state_sort = []
    states = dict()
    
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'State' and row[2] != '':
                state_unsort.append(row[2])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()
    ## 2. USING CPA

    state_unsort = []
    state_sort = []
    states = dict()

    print('Using .CPA breakdown')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != 'Using .CPA' and row[5] != '':
                state_unsort.append(row[5])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2)) + '%')
        print()
    print()
    print()
    # 3. Logo Style

    state_unsort = []
    state_sort = []
    states = dict()

    print('Logo Style breakdown')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[7] != 'Logo style' and row[7] != '':
                state_unsort.append(row[7])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()
    # 4. Primary logo

    state_unsort = []
    state_sort = []
    states = dict()

    print('Primary logo breakdown')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[8] != 'Primary Logo colour' and row[8] != '':
                state_unsort.append(row[8])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()

    # 5. Secondary logo

    state_unsort = []
    state_sort = []
    states = dict()

    print('Secondary logo breakdown')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[9] != 'Secondary Logo Colour' and row[9] != '':
                state_unsort.append(row[9])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()

    
    # 6. Name Style

    state_unsort = []
    state_sort = []
    states = dict()

    print('Name breakdown')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[10] != 'Name Style' and row[10] != '':
                state_unsort.append(row[10])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()

     
    # 7. Brand Persona

    state_unsort = []
    state_sort = []
    states = dict()

    print('Brand breakdown (cat 1)')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[11] != 'Brand Personality - Subcategory 1' and row[11] != '':
                state_unsort.append(row[11])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()

    # 8. Brand Persona

    state_unsort = []
    state_sort = []
    states = dict()

    print('Brand breakdown (cat 2)')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[12] != 'Brand Personality - Subcategory 2' and row[12] != '':
                state_unsort.append(row[12])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()

    # 9. Website color

    state_unsort = []
    state_sort = []
    states = dict()

    print('Website main color')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[13] != 'Website main colour' and row[13] != '':
                state_unsort.append(row[13])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()

    # 10. Website  second color

    state_unsort = []
    state_sort = []
    states = dict()

    print('Website second color')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[14] != 'Website secondary colour' and row[14] != '':
                state_unsort.append(row[14])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)

    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(states[i])
        print()
    print()
    print()

    # 11. Video on homepage?

    state_unsort = []
    state_sort = []
    states = dict()

    print('Video on homepage?')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[17] != 'Video on Homepage' and row[17] != '':
                state_unsort.append(row[17])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()
    print()


    # 12. Video on Site?

    state_unsort = []
    state_sort = []
    states = dict()

    print('Video on site?')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[18] != 'Video on Site' and row[18] != '':
                state_unsort.append(row[18])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()
    print()

    # 13. Photography

    state_unsort = []
    state_sort = []
    states = dict()

    print('Type of photography')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[19] != 'Photography Tone of Voice (ppl, scenery, abstract, cheesy stock, actual ppl in firm)' and row[19] != '':
                state_unsort.append(row[19])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()
    print()

    # 14. Blog

    state_unsort = []
    state_sort = []
    states = dict()

    print('Blog, insights, both, or neither?')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[21] != 'Blog, Insights, or Both in Navigation?' and row[21] != '':
                state_unsort.append(row[21])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()
    print()

    # 15. Blog w Original Content?

    state_unsort = []
    state_sort = []
    states = dict()

    print('Blog w original content')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[22] != 'Blog w/ Original Content?' and row[22] != '' and row[22] != 'Thought Leadership':
                state_unsort.append(row[22])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()
    print()

     # 16. Original resources

    state_unsort = []
    state_sort = []
    states = dict()

    print('Original resources')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[24] != 'Original Resources/ Downloadables (ebooks, guides, whitepapers)' and row[24] != '':
                state_unsort.append(row[24])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()
    print()

    # 17. Podcast

    state_unsort = []
    state_sort = []
    states = dict()

    print('Podcast')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[25] != 'Podcast' and row[25] != '':
                state_unsort.append(row[25])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()

    # 18. Webinars

    state_unsort = []
    state_sort = []
    states = dict()

    print('W')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[26] != 'Webinars (past, present, both)' and row[26] != '':
                state_unsort.append(row[26])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()

    # 19. Newsletter Sign-up

    state_unsort = []
    state_sort = []
    states = dict()

    print('Newsletter Sign-up')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[27] != 'Newsletter Sign-up' and row[27] != '' and row[27] != 'Conversions':
                state_unsort.append(row[27])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()

    # 20. Contact Form/Link

    state_unsort = []
    state_sort = []
    states = dict()

    print('Contact Form/Link')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[28] != 'Contact Form/Link' and row[28] != '':
                state_unsort.append(row[28])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()

    # 21. Book a Call/Phone link

    state_unsort = []
    state_sort = []
    states = dict()

    print('Book a Call/Phone link')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[29] != 'Book a Call/Phone link' and row[29] != '':
                state_unsort.append(row[29])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()

    # 22. Submit an RFP

    state_unsort = []
    state_sort = []
    states = dict()

    print('Submit an RFP')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[30] != 'Submit an RFP' and row[30] != '':
                state_unsort.append(row[30])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()

    # 23.Chatbox
    
    state_unsort = []
    state_sort = []
    states = dict()

    print('Chatbox')
    print()
    print()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')


        for row in reader:
            if row[31] != 'Chatbox' and row[31] != '':
                state_unsort.append(row[31])

    for i in state_unsort:
        if i not in state_sort:
            state_sort.append(i)
    
    for i in state_sort:
        j = state_unsort.count(i)
        states[i] = j
        print(i)
        print(str(round(100*states[i]/533,2))+'%')
        print()
    print()

    
print("Analysis and Python code by Benjamin Stager")
print("Data Scientist, Winding River Consulting, 2022")



analysis_top_firms('top500final.csv')
