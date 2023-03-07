# Similar to S+H, we will be building a CSV reader that takes in specifics
    # regarding Strothman's top 100 client data

import csv
def strothman(file_name):

    # 1. General analysis
    # 2. Assurance
    # 3. Tax
    # 4. Bookkeping

    # Instead of segmenting every industry, target performers
    # Spreadsheet is transposed, client is only listed once with certain
    #   blocks

    # Industry wide totals analysis

    #### NOTES SECTION

    
    # 1. KEEP IN MIND, this is only using the totals column
    # 2.

    ######## TOTALS ###########

    

    print('TOTAL ANALYSIS')
    print()
    print()
    
    print("General analysis")
    print()
    grand_total = 6745195.88
    grand_billings = 6073223.07
    assurance_total = 3797090.78
    assurance_billed = 3189001.21
    tax_total = 1544938.57
    tax_billed = 1427976.85
    bookkeeping_total = 418289.65
    bookkeeping_billed = 381726.4
    consulting_total = 889646.38
    consulting_billed = 868582.79
    valuations_total = 38098.5
    valuations_billed = 38832.78

    # Total billing analysis

    clients = dict()


    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[29] != '-':
                clients[row[2]] = float(row[29])
    
    print('Total billing percentage by client:')
    print()
    print()
    for i in clients.keys():
        print(i)
        print(str(round(100*clients[i]/grand_total,1))+"%")
        print()

    print()
    print()

    # Service analysis
    
    services = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] == 'Grand Total':
                services['Assurance'] = 3797090.78
                services['Tax'] = 1544938.57
                services['Bookkeeping / CFO Advisory'] = 418289.65
                services['Business Consulting / Expense'] = 889646.38
                services['Valuations'] = 38098.50
                services['Special'] = 57132.00

    data = []
    print()
    print('Service analysis')
    print()
    for i in services.keys():
        print(i)
        print(str(round(100*services[i]/grand_total,2)) + '%')
        print()
        x = []
        x.append(i)
        x.append(round(100*services[i]/grand_total,2))
        data.append(x)
        
    print()

    

    header = ['Service','% of totals']
    with open('service.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

    
    # Industry analysis
    print('Industry analysis')
    print()
    ind = []
    ind_res = []
    ind_revs = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != 'Industry' and row[5] != 'Grand Total' and row[5] != '':
                ind.append(row[5])

    for i in ind:
        if i not in ind_res:
            ind_res.append(i)

    for i in ind_res:
        ind_revs[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] in ind_revs.keys() and row[5] != 'Industry' and row[5] != '' and row[5] != 'Grand Total' and row[29] != '-':
                ind_revs[row[5]] += float(row[6])

    data = []
    for i in ind_revs:
        print(i)
        print('$' + str(ind_revs[i]))
        print(str(round(100*ind_revs[i]/grand_total,1)) + '%')
        x = []
        x.append(i)
        x.append(round(100*ind_revs[i]/grand_total,1))
        data.append(x)
        print()

    header = ['Industry','% of totals']
    with open('industry.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

    
    # Assurance analysis

    # First print each companies assurance percentage of total assurance revs
    # Each companys assurance over billings percentage
    # Segment assurance by industry as well, makes up for ~62% of total revs

    client_assurance = dict()


    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[9] != '':
                client_assurance[row[2]] = float(row[8])
    print()
    print()
    print('Assurance analysis')
    print()

    for i in client_assurance.keys():
        print(i)
        print('$' + str(client_assurance[i]))
        print(str(round(100*client_assurance[i]/assurance_total,2))+'%')
        print()

    print('Assurance breakdown by industry')
    print()

    assurance_ind = dict()

    for i in ind_res:
        assurance_ind[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] in assurance_ind.keys() and row[5] != 'Industry' and row[5] != '' and row[5] != 'Grand Total' and row[9]!= '':
                assurance_ind[row[5]] += float(row[8])   

    data =[]
    for i in assurance_ind.keys():
        print(i)
        print('$' + str(round(assurance_ind[i],2)))
        print(str(round(assurance_ind[i]*100/assurance_total,2)) + '%')
        x = []
        x.append(i)
        x.append(round(assurance_ind[i]*100/assurance_total,2))
        data.append(x)
        
        print()
    #maybe include real percentage by industry (!!!!) see below, or real/billed

    header = ['Industry','% of Assurance totals']
    with open('assurance.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
    
    # Tax analysis (company wide and industry)

    print('Tax analysis by firm')

    client_tax = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != '' and row[2] != 'Client Name':
                client_tax[row[2]] = float(row[6])

    print()
    for i in client_tax.keys():
        print(i)
        print(client_tax[i])
        print(str(round(100*client_tax[i]/grand_total,2)) + '%')
        print()


    
    print()
    print("Tax analysis by industry")
    print()
    tax_ind = dict()

    for i in ind_res:
        tax_ind[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] in tax_ind.keys() and row[5] != 'Industry' and row[5] != '' and row[5] != 'Grand Total' and row[11]!= '':
                tax_ind[row[5]] += float(row[11])

    for i in tax_ind.keys():
        print(i)
        print('$' + str(round(tax_ind[i],2)))
        print(str(round(tax_ind[i]*100/tax_total,2)) + '%')
        print()

    # Book keeping Analysis

    print('Company wide book keeping analysis')
    print()

    
    client_bookkeeping = dict()
    bookkeeping_ind = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[14] != '':
                client_bookkeeping[row[2]] = float(row[14])

    for i in client_bookkeeping.keys():
        print(i)
        print('$' + str(client_bookkeeping[i]))
        print(str(round(100*client_bookkeeping[i]/bookkeeping_total,2)) + '%')
        print()


    print('Industry book keeping analysis')
    print()

    for i in ind_res:
        bookkeeping_ind[i] = 0

        
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != '' and row[5] != 'Industry' and row[14] != '' and row[5] in bookkeeping_ind.keys():
                bookkeeping_ind[row[5]] += float(row[14])

    for i in bookkeeping_ind.keys():
        print(i)
        print('$' + str(bookkeeping_ind[i]))
        print(str(round(bookkeeping_ind[i]*100/bookkeeping_total,2)) + '%')
        print()
    print()

    # Business Consulting / Expense analysis

    print('Business Consulting / Expense analysis')
    print()
    print()


    client_consulting = dict()
    consulting_ind = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[17] != '':
                client_consulting[row[2]] = float(row[17])

    for i in client_consulting.keys():
        print(i)
        print('$' + str(client_consulting[i]))
        print(str(round(100*client_consulting[i]/consulting_total,2))+'%')
        print()

    for i in ind_res:
        consulting_ind[i] = 0

        
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != '' and row[5] != 'Industry' and row[17] != '' and row[5] in consulting_ind.keys():
                consulting_ind[row[5]] += float(row[17])

    for i in consulting_ind.keys():
        print(i)
        print('$' + str(consulting_ind[i]))
        print(str(round(100*consulting_ind[i]/consulting_total,2)) + '%')
        print()
    print()

    # Valuations analysis

    print('Valuations')
    print()
    print()


    client_valuations = dict()
    valuations_ind = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[20] != '':
                client_valuations[row[2]] = float(row[20])

    for i in client_valuations.keys():
        print(i)
        print('$' + str(client_valuations[i]))
        print(str(round(100*client_valuations[i]/valuations_total,2))+'%')
        print()

    for i in ind_res:
        valuations_ind[i] = 0

        
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != '' and row[5] != 'Industry' and row[20] != '' and row[5] in valuations_ind.keys():
                valuations_ind[row[5]] += float(row[20])

    for i in valuations_ind.keys():
        print(i)
        print('$' + str(round(valuations_ind[i],2)))
        print(str(round(valuations_ind[i]*100/valuations_total,2)) + '%')
        print()
    print()
        

    # Don't understand progress bills, skip







    ## END OF TOTALS SEGMENTATION



    # Now we divide it by the billed column,
    # same procedure just one column apart

    # As

    print('BILLING ANALYSIS')
    print()
    print()

    print('Service analysis')
    print()

    
    services = dict()
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')
    

        for row in reader:
            if row[5] == 'Grand Total':
                services['Assurance'] = 3189001.21
                services['Tax'] = 1427976.85
                services['Bookkeeping / CFO Advisory'] = 381726.4
                services['Business Consulting / Expense'] = 868582.79
                services['Valuations'] = 38832.78
                services['Progress Bills'] = 118273.04
                services['Special'] = 48830
            
    clients = dict()


    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[30] != '':
                clients[row[2]] = float(row[30])
    
    print('Total billing percentage by client:')
    print()
    print()
    for i in clients.keys():
        print(i)
        print(str(round(100*clients[i]/grand_billings,1))+"%")
        print()

    print()
    print()

    print()
    print('Service analysis')
    print()
    for i in services.keys():
        print(i)
        print(str(round(100*services[i]/grand_billings,2)) + '%')
        print()

    # Industry analysis
    
    print('Industry analysis')
    print()
    ind = []
    ind_res = []
    ind_revs = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != 'Industry' and row[5] != 'Grand Total' and row[5] != '':
                ind.append(row[5])

    for i in ind:
        if i not in ind_res:
            ind_res.append(i)

    for i in ind_res:
        ind_revs[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] in ind_revs.keys() and row[5] != 'Industry' and row[5] != '' and row[5] != 'Grand Total' and row[30] != '-':
                ind_revs[row[5]] += float(row[30])

    for i in ind_revs:
        print(i)
        print('$' + str(ind_revs[i]))
        print(str(round(100*ind_revs[i]/grand_billings,1)) + '%')
        print()    


    # Assurance

    client_assurance = dict()


    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[9] != '':
                client_assurance[row[2]] = float(row[9])
    print()
    print()
    print('Assurance analysis')
    print()

    for i in client_assurance.keys():
        print(i)
        print('$' + str(client_assurance[i]))
        print(str(round(100*client_assurance[i]/assurance_billed,2))+'%')
        print()

    print('Assurance breakdown by industry')
    print()

    assurance_ind = dict()

    for i in ind_res:
        assurance_ind[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] in assurance_ind.keys() and row[5] != 'Industry' and row[5] != '' and row[5] != 'Grand Total' and row[9]!= '':
                assurance_ind[row[5]] += float(row[9])   


    for i in assurance_ind.keys():
        print(i)
        print('$' + str(round(assurance_ind[i],2)))
        print(str(round(assurance_ind[i]*100/assurance_billed,2)) + '%')
        print()


    # Tax analysis (company wide and industry)

    print('Tax analysis by firm')

    client_tax = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != '' and row[2] != 'Client Name' and row[29] != '-':
                client_tax[row[2]] = float(row[29])

    print()
    for i in client_tax.keys():
        print(i)
        print(client_tax[i])
        print(str(round(100*client_tax[i]/tax_billed,2)) + '%')
        print()


    
    print()
    print("Tax analysis by industry")
    print()
    tax_ind = dict()

    for i in ind_res:
        tax_ind[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] in tax_ind.keys() and row[5] != 'Industry' and row[5] != '' and row[5] != 'Grand Total' and row[12]!= '':
                tax_ind[row[5]] += float(row[12])

    for i in tax_ind.keys():
        print(i)
        print('$' + str(round(tax_ind[i],2)))
        print(str(round(tax_ind[i]*100/tax_billed,2)) + '%')
        print()



    # Bookkeeping
    print('Company wide book keeping analysis')
    print()

    
    client_bookkeeping = dict()
    bookkeeping_ind = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[15] != '':
                client_bookkeeping[row[2]] = float(row[15])

    for i in client_bookkeeping.keys():
        print(i)
        print('$' + str(client_bookkeeping[i]))
        print(str(round(100*client_bookkeeping[i]/bookkeeping_billed,2)) + '%')
        print()


    print('Industry book keeping analysis')
    print()

    for i in ind_res:
        bookkeeping_ind[i] = 0

        
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != '' and row[5] != 'Industry' and row[15] != '' and row[5] in bookkeeping_ind.keys():
                bookkeeping_ind[row[5]] += float(row[15])

    for i in bookkeeping_ind.keys():
        print(i)
        print('$' + str(bookkeeping_ind[i]))
        print(str(round(bookkeeping_ind[i]*100/bookkeeping_total,2)) + '%')
        print()
    print()

    
    # Business Consulting / Expense analysis

    print('Business Consulting / Expense analysis')
    print()
    print()


    client_consulting = dict()
    consulting_ind = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[18] != '':
                client_consulting[row[2]] = float(row[18])

    for i in client_consulting.keys():
        print(i)
        print('$' + str(client_consulting[i]))
        print(str(round(100*client_consulting[i]/consulting_billed,2))+'%')
        print()

    for i in ind_res:
        consulting_ind[i] = 0

        
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != '' and row[5] != 'Industry' and row[18] != '' and row[5] in consulting_ind.keys():
                consulting_ind[row[5]] += float(row[18])

    for i in consulting_ind.keys():
        print(i)
        print('$' + str(consulting_ind[i]))
        print(str(round(consulting_ind[i]*100/consulting_billed,2)) + '%')
        print()
    print()


    # Valuations analysis

    print('Valuations')
    print()
    print()


    client_valuations = dict()
    valuations_ind = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[2] != 'Client Name' and row[2] != '' and row[21] != '':
                client_valuations[row[2]] = float(row[21])

    for i in client_valuations.keys():
        print(i)
        print('$' + str(client_valuations[i]))
        print(str(round(100*client_valuations[i]/valuations_billed,2))+'%')
        print()

    for i in ind_res:
        valuations_ind[i] = 0

        
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        for row in reader:
            if row[5] != '' and row[5] != 'Industry' and row[21] != '' and row[5] in valuations_ind.keys():
                valuations_ind[row[5]] += float(row[21])

    for i in valuations_ind.keys():
        print(i)
        print('$' + str(round(valuations_ind[i],2)))
        print(str(round(valuations_ind[i]*100/valuations_billed,2)) + '%')
        print()
    print()


    
strothman('StrothmanTop100.csv')
