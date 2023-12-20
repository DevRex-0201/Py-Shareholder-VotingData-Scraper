import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

url = "https://central-webd.proxydisclosure.com/WebDisclosure/wdMeetingList"

indexs = [[18192, "JPMorgan 100 Percent U.S. Treasury Securities Money Market Fund"], [28157, "JPMorgan Active China ETF"], [28143, "JPMorgan Active Growth ETF"], [28144, "JPMorgan Active Small Cap Value ETF"], [26589, "JPMorgan Active Value ETF"], [25309, "JPMorgan ActiveBuilders Emerging Markets Equity ETF"], [26590, "JPMorgan ActiveBuilders International Equity ETF"], [26591, "JPMorgan ActiveBuilders U.S. Large Cap Equity ETF"], [23679, "JPMorgan BetaBuilders 1-5 Year U.S. Aggregate Bond ETF"], [23838, "JPMorgan BetaBuilders Canada ETF"], [23822, "JPMorgan BetaBuilders Developed Asia ex-Japan ETF"], [28156, "JPMorgan BetaBuilders Emerging Markets Equity ETF"], [22957, "JPMorgan BetaBuilders Europe ETF"], [24736, "JPMorgan BetaBuilders International Equity ETF"], [22958, "JPMorgan BetaBuilders Japan ETF"], [22868, "JPMorgan BetaBuilders MSCI US REIT ETF"], [23678, "JPMorgan BetaBuilders U.S. Aggregate Bond ETF"], [23849, "JPMorgan BetaBuilders U.S. Equity ETF"], [24588, "JPMorgan BetaBuilders U.S. Mid Cap Equity ETF"], [25310, "JPMorgan BetaBuilders U.S. Small Cap Equity ETF"], [28151, "JPMorgan BetaBuilders U.S. TIPS 0-5 Year ETF"], [28152, "JPMorgan BetaBuilders U.S. Treasury Bond 1-3 Year ETF"], [28150, "JPMorgan BetaBuilders U.S. Treasury Bond 20+ Year ETF"], [28145, "JPMorgan BetaBuilders U.S. Treasury Bond 3-10 Year ETF"], [22427, "JPMorgan BetaBuilders USD High Yield Corporate Bond ETF"], [23681, "JPMorgan BetaBuilders USD Investment Grade Corporate Bond ETF"], [18197, "JPMorgan California Municipal Money Market Fund"], [18198, "JPMorgan California Tax Free Bond Fund"], [25311, "JPMorgan Carbon Transition U.S. Equity ETF"], [26592, "JPMorgan Climate Change Solutions ETF"], [18308, "JPMorgan Core Bond Fund"], [18172, "JPMorgan Core Bond Trust"], [22426, "JPMorgan Core Focus SMA Fund"], [23677, "JPMorgan Core Plus Bond ETF"], [18309, "JPMorgan Core Plus Bond Fund"], [18201, "JPMorgan Corporate Bond Fund"], [18206, "JPMorgan Diversified Fund"], [20929, "JPMorgan Diversified Return Emerging Markets Equity ETF"], [20931, "JPMorgan Diversified Return International Equity ETF"], [21793, "JPMorgan Diversified Return U.S. Equity ETF"], [21796, "JPMorgan Diversified Return U.S. Mid Cap Equity ETF"], [22423, "JPMorgan Diversified Return U.S. Small Cap Equity ETF"], [18214, "JPMorgan Emerging Markets Debt Fund"], [18215, "JPMorgan Emerging Markets Equity Fund"], [23851, "JPMorgan Emerging Markets Research Enhanced Equity Fund"], [28559, "JPMorgan Equity Focus ETF"], [18217, "JPMorgan Equity Focus Fund"], [18310, "JPMorgan Equity Income Fund"], [18311, "JPMorgan Equity Index Fund"], [24589, "JPMorgan Equity Premium Income ETF"], [23684, "JPMorgan Equity Premium Income Fund"], [18244, "JPMorgan Europe Dynamic Fund"], [18219, "JPMorgan Federal Money Market Fund"], [18220, "JPMorgan Floating Rate Income Fund"], [18221, "JPMorgan Global Allocation Fund"], [18222, "JPMorgan Global Bond Opportunities Fund"], [18312, "JPMorgan Government Bond Fund"], [18171, "JPMorgan Growth Advantage Fund"], [25441, "JPMorgan Hedged Equity 2 Fund"], [25440, "JPMorgan Hedged Equity 3 Fund"], [19608, "JPMorgan Hedged Equity Fund"], [18313, "JPMorgan High Yield Fund"], [28558, "JPMorgan High Yield Municipal ETF"], [18291, "JPMorgan High Yield Municipal Fund"], [18230, "JPMorgan Income Builder Fund"], [26593, "JPMorgan Income ETF"], [19609, "JPMorgan Income Fund"], [23685, "JPMorgan Inflation Managed Bond ETF"], [22855, "JPMorgan Institutional Tax Free Money Market Fund"], [18175, "JPMorgan Insurance Trust Core Bond Portfolio"], [20728, "JPMorgan Insurance Trust Global Allocation Portfolio"], [20729, "JPMorgan Insurance Trust Income Builder Portfolio"], [18183, "JPMorgan Insurance Trust Mid Cap Value Portfolio"], [18181, "JPMorgan Insurance Trust Small Cap Core Portfolio"], [18182, "JPMorgan Insurance Trust U.S. Equity Portfolio"], [18174, "JPMorgan Intermediate Bond Trust"], [22428, "JPMorgan International Bond Opportunities ETF"], [18235, "JPMorgan International Equity Fund"], [18239, "JPMorgan International Focus Fund"], [24734, "JPMorgan International Growth ETF"], [23680, "JPMorgan International Hedged Equity Fund"], [26604, "JPMorgan International Research Enhanced Equity ETF"], [18240, "JPMorgan International Value Fund"], [18316, "JPMorgan Investor Balanced Fund"], [18317, "JPMorgan Investor Conservative Growth Fund"], [18318, "JPMorgan Investor Growth &amp; Income Fund"], [18319, "JPMorgan Investor Growth Fund"], [18320, "JPMorgan Large Cap Growth Fund"], [18321, "JPMorgan Large Cap Value Fund"], [28557, "JPMorgan Limited Duration Bond ETF"], [18322, "JPMorgan Limited Duration Bond Fund"], [18323, "JPMorgan Liquid Assets Money Market Fund"], [24739, "JPMorgan Macro Opportunities Fund"], [18249, "JPMorgan Managed Income Fund"], [26603, "JPMorgan Market Expansion Enhanced Equity ETF"], [18251, "JPMorgan Mid Cap Equity Fund"], [18327, "JPMorgan Mid Cap Growth Fund"], [18170, "JPMorgan Mid Cap Value Fund"], [18328, "JPMorgan Mortgage-Backed Securities Fund"], [23683, "JPMorgan Municipal ETF"], [18331, "JPMorgan Municipal Money Market Fund"], [26602, "JPMorgan Nasdaq Equity Premium Income ETF"], [18233, "JPMorgan National Municipal Income Fund"], [18254, "JPMorgan New York Municipal Money Market Fund"], [18255, "JPMorgan New York Tax Free Bond Fund"], [20731, "JPMorgan Opportunistic Equity Long Short Fund"], [26588, "JPMorgan Preferred and Income Securities Fund"], [18256, "JPMorgan Prime Money Market Fund"], [26598, "JPMorgan Realty Income ETF"], [18260, "JPMorgan Research Market Neutral Fund"], [18315, "JPMorgan SMID Cap Equity Fund"], [23686, "JPMorgan Securities Lending Money Market Fund"], [18334, "JPMorgan Short Duration Bond Fund"], [25312, "JPMorgan Short Duration Core Plus ETF"], [18262, "JPMorgan Short Duration Core Plus Fund"], [18335, "JPMorgan Short-Intermediate Municipal Bond Fund"], [18211, "JPMorgan Small Cap Blend Fund"], [18264, "JPMorgan Small Cap Equity Fund"], [18342, "JPMorgan Small Cap Growth Fund"], [18263, "JPMorgan Small Cap Sustainable Leaders Fund"], [18336, "JPMorgan Small Cap Value Fund"], [18269, "JPMorgan SmartRetirement 2020 Fund"], [18270, "JPMorgan SmartRetirement 2025 Fund"], [18271, "JPMorgan SmartRetirement 2030 Fund"], [18272, "JPMorgan SmartRetirement 2035 Fund"], [18273, "JPMorgan SmartRetirement 2040 Fund"], [18274, "JPMorgan SmartRetirement 2045 Fund"], [18275, "JPMorgan SmartRetirement 2050 Fund"], [18276, "JPMorgan SmartRetirement 2055 Fund"], [22421, "JPMorgan SmartRetirement 2060 Fund"], [28147, "JPMorgan SmartRetirement 2065 Fund"], [24590, "JPMorgan SmartRetirement Blend 2015 Fund"], [18278, "JPMorgan SmartRetirement Blend 2020 Fund"], [18279, "JPMorgan SmartRetirement Blend 2025 Fund"], [18280, "JPMorgan SmartRetirement Blend 2030 Fund"], [18281, "JPMorgan SmartRetirement Blend 2035 Fund"], [18282, "JPMorgan SmartRetirement Blend 2040 Fund"], [18283, "JPMorgan SmartRetirement Blend 2045 Fund"], [18284, "JPMorgan SmartRetirement Blend 2050 Fund"], [18285, "JPMorgan SmartRetirement Blend 2055 Fund"], [22420, "JPMorgan SmartRetirement Blend 2060 Fund"], [28149, "JPMorgan SmartRetirement Blend 2065 Fund"], [18286, "JPMorgan SmartRetirement Blend Income Fund"], [18287, "JPMorgan SmartRetirement Income Fund"], [28153, "JPMorgan Social Advancement ETF"], [18288, "JPMorgan Strategic Income Opportunities Fund"], [28154, "JPMorgan Sustainable Consumption ETF"], [28155, "JPMorgan Sustainable Infrastructure ETF"], [28560, "JPMorgan Sustainable Municipal Income ETF"], [18330, "JPMorgan Sustainable Municipal Income Fund"], [18290, "JPMorgan Tax Aware Equity Fund"], [18293, "JPMorgan Tax Aware Real Return Fund"], [18337, "JPMorgan Tax Free Bond Fund"], [18295, "JPMorgan Tax Free Money Market Fund"], [18298, "JPMorgan Total Return Fund"], [18247, "JPMorgan U.S. Applied Data Science Value Fund"], [22921, "JPMorgan U.S. Dividend ETF"], [18300, "JPMorgan U.S. Equity Fund"], [18245, "JPMorgan U.S. GARP Equity Fund"], [18339, "JPMorgan U.S. Government Money Market Fund"], [18301, "JPMorgan U.S. Large Cap Core Plus Fund"], [22922, "JPMorgan U.S. Minimum Volatility ETF"], [22923, "JPMorgan U.S. Momentum Factor ETF"], [22924, "JPMorgan U.S. Quality Factor ETF"], [18205, "JPMorgan U.S. Research Enhanced Equity Fund"], [18304, "JPMorgan U.S. Small Company Fund"], [18242, "JPMorgan U.S. Sustainable Leaders Fund"], [18341, "JPMorgan U.S. Treasury Plus Money Market Fund"], [22925, "JPMorgan U.S. Value Factor ETF"], [18228, "JPMorgan U.S. Value Fund"], [22854, "JPMorgan USD Emerging Markets Sovereign Bond ETF"], [22629, "JPMorgan Ultra-Short Income ETF"], [21892, "JPMorgan Ultra-Short Municipal Fund"], [23682, "JPMorgan Ultra-Short Municipal Income ETF"], [18253, "JPMorgan Unconstrained Debt Fund"], [18305, "JPMorgan Value Advantage Fund"], [18186, "Undiscovered Managers Behavioral Value Fund"]]

pattern = re.compile(r"'([^']*)'")

# Create an empty list to store the data
data_list = []

for index in indexs:
    rec_num = 1
    
    form_fund = {
         'siteId': 'JPMFunds',
        'fundId': index[0],
        'fundName': index[1],
        'fundIdTmp': '',
        'previewkey': '',
        'currentPageNumber': rec_num,
        'meetingId': '',
        'sortByColumn': 'COMPANY_NAME',
        'sortingOrder': 'ASC',
        'fundCompNameSection': '',
        'tickerSymbol': '',
        'companyName': '',
        'companyNameStartsWith': '',
        'meetingDate': '',
        'meetingTypeDesc': '',
        'securityId': '',
        'tickerSymbolPage3': '',
        'isin': '',
        'compNamePage2To3': '',
    }   
    while True:
        # Send the POST request
        response = requests.post(url, data=form_fund)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <a> elements with class "MeetingListLink"
            meeting_links = soup.find_all('tr', class_='Row')

            # Check if there are no meeting links
            if not meeting_links:
                print("No meeting links found. Breaking out of the loop.")
                break

            # Extract and print the "href" attribute values
            for link in meeting_links: 
                href_value = link.find('a').get('href')                               
                matches = pattern.findall(href_value)
                cleaned_matches = [match.strip() for match in matches]                
                # cleaned_string = ', '.join(cleaned_matches)
                if matches:
                    id_numbers = cleaned_matches                    
                    form_detail = {
                        'siteId': 'JPMFunds',
                        'fundId': index[0],
                        'fundName': index[1],
                        'fundIdTmp': '',
                        'previewkey': '',
                        'currentPageNumber': rec_num,
                        'meetingId': id_numbers[0],
                        'sortByColumn': 'COMPANY_NAME',
                        'sortingOrder': 'ASC',
                        'fundCompNameSection': '',
                        'tickerSymbol': '',
                        'companyName': '',
                        'companyNameStartsWith': '',
                        'meetingDate': id_numbers[1],
                        'meetingTypeDesc': id_numbers[2],
                        'securityId': id_numbers[3],
                        'tickerSymbolPage3': id_numbers[4],
                        'isin': id_numbers[5],
                        'compNamePage2To3': id_numbers[6],
                    }
                    url_detail = "https://central-webd.proxydisclosure.com/WebDisclosure/wdMeetingDetail"                
                    # Send the POST request
                    response_detail = requests.post(url_detail, data=form_detail)
                    # Check if the request was successful (status code 200)
                    if response_detail.status_code == 200:
                        # print(form_detail)
                        # Parse the HTML content with BeautifulSoup
                        soup_detail = BeautifulSoup(response_detail.text, 'html.parser')
                        # print(soup_detail)
                        odd_rows = soup_detail.find_all('tr')
                        company_name = soup_detail.find('h1').get_text().replace('  ', '').replace('\n', '')
                        # print(odd_rows)
                        data_field = soup_detail.find_all('label', class_='data-field')
                       
                        ticker = data_field[3].get_text().replace('  ', '').replace('\n', '')
                        meeting_date = data_field[0].get_text().replace('  ', '').replace('\n', '')
                        agenda_number = data_field[4].get_text().replace('  ', '').replace('\n', '')
                        security_id = data_field[2].get_text().replace('  ', '').replace('\n', '')
                        meeting_type = data_field[1].get_text().replace('  ', '').replace('\n', '')
                        isin = data_field[5].get_text().replace('  ', '').replace('\n', '')
                        fund = index[1]
                        
                        # print([company_name, ticker, meeting_date, agenda_number, security_id, meeting_type, isin])
                        # fund_name = soup_detail.find('span', id='VPFundNameNoImage').get_text().replace('  ', '').replace('\n', '').replace('- ', '')                             
                        
                        # Extract and print the inner text of each "td" element
                        for row in odd_rows:    
                            if row.has_attr('class'):
                                td_elements = row.find_all('td')     
                                item_number = td_elements[0].get_text().replace('  ', '').replace('\n', '')          
                                proposal = td_elements[1].find('div').get_text().replace('  ', '').replace('\n', '')          
                                type = td_elements[2].get_text().replace('  ', '').replace('\n', '')          
                                vote = td_elements[3].get_text().replace('  ', '').replace('\n', '')          
                                for_against = td_elements[4].get_text().replace('  ', '').replace('\n', '')          
                                
                                print([company_name, ticker, meeting_date, agenda_number, security_id, meeting_type, isin, item_number, proposal, type, vote, for_against, fund])
                                # Append the data to the list
                                data_list.append([company_name, ticker, meeting_date, agenda_number, security_id, meeting_type, isin, item_number, proposal, type, vote, for_against, fund])
                    
                    # print(soup_detail)
            
            # Increase RecNum for the next request
            form_fund['currentPageNumber'] += 1            
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            print(response.text)
            break  # Break the loop if the response code is not 200
print(data_list)
# Create a DataFrame from the list
df = pd.DataFrame(data_list, columns=['Company Name', 'Ticker', 'Meeting Date', 'Agenda Number', 'Security ID', 'Meeting Type', 'Isin', 'Item Number', 'Proposal', 'Type', 'Vote', 'For/Against', 'Fund'])

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)
