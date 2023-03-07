
# CSV handler for S+H ACTUAL RUN

import csv


# Define a function that reads in a file name/CSV

def firm_analysis(file_name):

    
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')

        clientGroup = []

        # Column aggregator process
        
        for row in reader:
            if row[2] != 'ClientGroup':
                if 'Total' not in row[2]:
                    clientGroup.append(row[2])

    res = []

    # Algorithm to remove repeats from a list
    for i in clientGroup:
        if i not in res:
            res.append(i)


    rev = dict()

    for i in res:
        rev[i] = 0

    # This algorithm is used for several parts of this code,
    # by targeting keys in the existing dictionary we can sum
    # revenues by key value and then from there pull more data
    # from that dictionary
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[9] != 'Invoiced':
                if row[2] in rev:
                    rev[row[2]] += float(row[9])

    
    print()
    print("TOTAL REVS BY CLIENT")
    print()
    for i in rev.keys():
        print(str(i)+": $" + str(rev[i]))
        print()


    print()
    print()


    # CONST Total revenue for S+H
    total = 19112838

    
    rev_pct = dict()


    # Simple algorithm for calculating revenue percentage
    for i in rev.keys():
        rev_pct[i] = float(100*float(rev[i]/total))

    print()
    print("PERCENT OF TOTAL REV BY CLIENT")
    print()
    for i in rev_pct.keys():
        print("Company: " + i)
        print("Percent of total invoices: " + str(round(rev_pct[i],1))+ "%")
        print()

    num = 0
    for i in rev.values():
        num += float(i)


    # Now we analyze the different type of service that S+H dpes

    tax_type = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[1] != 'Service' or row[1] != ' ':
                tax_type.append(row[1])

    tax_res = []


    # Build directory for different services
    
    for i in tax_type:
        if i not in tax_res:
            tax_res.append(i)

    # Cleanup
    
    if '' in tax_res:
        tax_res.remove('')
    if 'Service' in tax_res:
        tax_res.remove('Service')

    tax_breakdown = dict()

    for i in tax_res:
        tax_breakdown[i] = 0

    # Revs for each type of tax, once again we can use this to calculate pct
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[9] != 'Invoiced':
                if row[1] in tax_breakdown:
                    tax_breakdown[row[1]] += float(row[9])
     
    
    print()
    print()

    data= []
    print("PERCENT OF REV BY SERVICE")
    print()
    for i in tax_breakdown.keys():
        print("Service:", i)
        print("Pct: " +str(round(100*int(tax_breakdown[i])/total,2))+"%")
        print()
        x = []
        x.append(i)
        x.append(tax_breakdown[i])
        data.append(x)


    header = ['Service','Invoice Amount']
    with open('service_bs.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        
        writer.writerow(header)

        writer.writerows(data)


    # Analysis for industry
    
    industry = []
    industry_res = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[5] != 'Industry':
                industry.append(row[5])

    for i in industry:
        if i not in industry_res:
            industry_res.append(i)

    if '' in industry_res:
        industry_res.remove('')

    print()
    print()


    industry_breakdown = dict()

    for i in industry_res:
        industry_breakdown[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[9] != 'Invoiced':
                if row[5] in industry_breakdown:
                    industry_breakdown[row[5]] += float(row[9])


    data = []
    print("PERCENT OF REV BY INDUSTRY")
    print()
    for i in industry_breakdown.keys():
        print("Industry:", i)
        print("Pct of invoices: "+ str(round(100*(industry_breakdown[i]/total),1))+'%')
        print()
        x = []
        x.append(i)
        x.append(industry_breakdown[i])
        data.append(x)

    header = ['Industry','Invoice Amount']
    with open('industry_REVS.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        
        writer.writerow(header)

        writer.writerows(data)
    
        
    



    #
    
    hsp_total = 0

    
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[5] == 'Hospitality':
                hsp_total += float(row[9])
    hospitality_subind = []

    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[5] == 'Hospitality':
                hospitality_subind.append(row[1])

    hsp_res = []

    for i in hospitality_subind:
        if i not in hsp_res:
            hsp_res.append(i)

    ## now we want total revenue break down by industry - break:
            ## into single key dictionary

    hsp_breakdown = dict()

    for i in hsp_res:
        hsp_breakdown[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[9] != 'Invoiced':
                if row[1] in hsp_breakdown.keys():
                    hsp_breakdown[row[1]] += float(row[9])

    print()
    print("PERCENT OF HOSPITALITY REV BY SUBINDUSTRY")
    print()
    for i in hsp_breakdown.keys():
        print("Subindustry:", i)
        print("Revenue pct: " + str(round(100*hsp_breakdown[i]/hsp_total,1)) +
              "%")
        print()

    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[5] == 'Hospitality':
                hospitality_subind.append(row[1])

    hsp_service = dict()

    for i in hospitality_subind:
        hsp_service[i] = hospitality_subind.count(i)

    # Next - top 3 performers percentage wise for total business tax rev
            # bottom 3 performers percentage wise for total business tax rev

    # We first want to identify what the total business tax revneue is

    btax_rev = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[1] == 'Business Tax':
                btax_rev += float(row[9])

    
    
    ind_btax = dict()

    for i in industry_res:
        ind_btax[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[1] == 'Business Tax' and row[5] in ind_btax.keys():
                ind_btax[row[5]] += float(row[9])
    print()
    print()
    print("BTAX BY INDUSTRY")
    print()

    data = []
    for i in ind_btax:
        print(i)
        print(str(round(100*ind_btax[i]/btax_rev,1))+"%")
        print()
        x = []
        x.append(i)
        x.append(round(100*ind_btax[i]/btax_rev,1))
        data.append(x)

    header = ['Industry','% of business tax invoices']
    with open('industryBTAX_SH.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)

        
        writer.writerow(header)

        writer.writerows(data)


    

    # We have a dictionary, each key is the industry, each company is b tax
        # revenue


    # Introducing other segmentation

    # 1. Segment audit by industry
    # 2. Segment real estate by service and subindustry
    # 3. Insurance and Trusts seem to be pain points, segment them by service?
    # 4. Average invoice per industry

    ind_audit = dict()
    total_audit = 0
    
    for i in industry_res:
        ind_audit[i] = 0

    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[1] == 'Audit' and row[8] != 'Invoiced':
                total_audit += float(row[9])

    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[1] == 'Audit' and row[5] in ind_audit.keys():
                ind_audit[row[5]] += float(row[9])

    
    
    
    print()
    print("AUDIT INVOICE PCT")
    print()
    for i in ind_audit.keys():
        print("Industry: ", i)
        print("Pct of audit invoices: " + str(round(ind_audit[i]*100/total_audit
                                                    ,2)) + '%')
        print()
                                                    
    # We want the average invoice per industry
    # Dictionary with industry as keys and average price per invoice
    
    print()
    print()

    ind_avg = dict()
    
    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if 'Total' in row[2]:
                row[2] = row[2].split(' ')
            
    
    for i in industry_breakdown.keys():
        ind_avg[i] = round(industry_breakdown[i]/industry.count(i),2)

    hsp_total = 0
    with open(file_name,'r') as file:
        reader = csv.reader(file, delimiter = ',')
        for row in reader:
            if row[5] == 'Hospitality':
                hsp_total += float(row[9])
    print("AVERAGE INVOICE PER INDUSTRY")
    print()
    for i in ind_avg:
        print('Industry:', i)
        print("$"+ str(ind_avg[i]))
        print()
        
    service = []
    service_res = []
    hospitality = dict()

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter =',')

        for row in reader:
            if row[1] != 'Service':
                service.append(row[1])

    for i in service:
        if i not in service_res:
            service_res.append(i)
    for i in service_res:
        hospitality[i] = 0

    with open(file_name, 'r') as file:
        reader = csv.reader(file, delimiter =',')

        for row in reader:
            if row[5] == 'Hospitality' and row[1] in hospitality.keys():
                hospitality[row[1]] += float(row[9])
    
    
        
    print()
    print("ANALYSIS")
    print()
    print()

    print("Top three firms for by total invoice percentage:")
    print("Argone: 6.1%")
    print("Edible: 3.0%")
    print("Mansfield: 2.9%")

    print()

    print("Top three services by total invoice percentage:")
    print("Business Tax: 42.8%")
    print("Audit: 22.7%")
    print("Individual Tax: 10.9%")

    print()

    print("Top three industries by total invoice percentage:")
    print("Hospitality: 12.2%")
    print("Service Companies: 11.4%")
    print("Individual: 11.4%")

    print()
    
    print("Lowest generators per category:")
    print("Firm: GasSouth, .4%")
    print("Service: Business, <.1%")
    print("Industry: Management Companies, .5%")

    print()
    print("Subindustry analysis of HOSPITALITY:")
    print()
    print("FRANCHISOR percentage of total hospitality invoices: 52.0%")
    print("RESTAURANT percentage of total hospitality invoices: 47.9%")
    print("OTHER percentage of total hospitality invoices: .1%")
    print()

    print()
    print("Service analysis of HOSPITALITY")
    print()
    for i in hsp_breakdown.keys():
        print("Service:", i)
        print("Deal percentage: " + str(round(100*hospitality[i]/(hsp_total),2)) +"%")
        print()
    print()
    print()
    print()

    print("Analysis of business tax invoices:")
    print()
    print()
    print("Total business tax invoices: $8,183,032")
    print("Percentage of total invoices by business tax: 42.81%")
    print()
    print("Top three industries under business tax invoices (by percentage):")
    print("Real Estate: 15.9%")
    print("Hospitality: 14.7%")
    print("Manufacturing: 14.2%")
    print()
    print("Bottom three industries under business tax invoices (by percentage):")
    print("Management Companies: 1.0%")
    print("Insurance: 0.7%")
    print("Trusts: 0.1%")
    
    print()
    print()
    print()
    
    print("Analysis and Python code by Benjamin Stager")
    print("Data Scientist, Winding River Consulting, 2022")
            
firm_analysis('sh.csv')

