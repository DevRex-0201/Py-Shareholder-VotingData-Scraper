import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

url = "https://vds.issproxy.com/MeetingList.php"

indexs = [17097, 24845, 6502, 24892, 6503, 21632, 6501, 39111, 11787, 50564, 11790, 23403, 11789, 11788, 50565, 17960, 19716, 17016, 8908, 18681, 17043, 17055, 1247, 58237, 18685, 17057, 21630, 15804, 18678, 17062, 17048, 2852, 16992, 39107, 16993, 17039, 17049, 18692, 18694, 33891, 19715, 2883, 2872, 16996, 11786, 33889, 17000, 39116, 39115, 39114, 58236, 50563, 24847, 50562, 17013, 6443, 6828, 17004, 1257, 6440, 17005, 11785, 17006, 17061, 42992, 17007, 17019, 15802, 51705, 16719, 17009, 6444, 47549, 42990, 47551, 39136, 39138, 39137, 42991, 28581, 28582, 17011, 17040, 17050, 15650, 42976, 21623, 35835, 19717, 2886, 17044, 17058, 15803, 35841, 6442, 39110, 1251, 2889, 39105, 17028, 17042, 17053, 2881, 42977, 16718, 2877, 6826, 42978, 39108, 39106, 1253, 18680, 35837, 30803, 17054, 2863, 18646, 17056, 18645, 51711, 17963, 17091, 17964, 17092, 17965, 17093, 17966, 28579, 35839, 17094, 39122, 39123, 39125, 39126, 39127, 39130, 39132, 39134, 39135, 39120, 17968, 17969, 17970, 17971, 17972, 17973, 17974, 27100, 35840, 17975, 2870, 34110, 2910, 8906, 2880, 15648, 17047, 1246, 17023, 15649, 21634, 30603, 33896, 17027, 21635, 16015, 2835, 2853, 2839, 16016, 16093, 16096, 16018, 16094, 16097, 16019, 16021, 16103, 16023, 16106, 16107, 16022, 16024, 17030, 17033, 17024, 2856, 17025, 17026, 39109, 21631, 18389, 39118, 39119, 17059, 34567, 24844, 21626, 51706, 17031, 30804, 39117, 17063, 16138, 17032, 16108, 28443, 39113, 51709, 39112, 27099, 16989, 17038, 30600, 17034, 16120, 42979, 42980, 42981, 42982, 42983, 42984, 24882, 15798, 18388, 1252, 21624, 18690, 17060, 39139, 33890, 17041, 17052, 35836, 51710, 17072, 17012, 19719, 2848, 2898, 39140, 2914, 47550, 17095, 2908, 23404, 27096, 51708, 51707, 18679, 17959, 30805, 17961, 18687, 24880, 27098, 18700, 27094, 27097, 18699, 42986, 42988, 42985, 42987, 42989, 17988, 17088, 16129, 17105, 2913, 2915, 17108, 2907, 2906, 2909, 17958, 17107, 2911, 17096]

pattern = re.compile(r'\((\d+),\s(\d+),\s(\d+)\)')

# Create an empty list to store the data
data_list = []

for index in indexs:
    print(index)
    rec_num = 1
    
    form_fund = {
        'CustomerID': 1615,
        'FundID': index,
        'MeetingListFundID': index,
        'SingleFund': 0,
        'FundFamilyID': 0,
        'SearchType': 1,
        'AlphaSearch': '',
        'SearchFor': '',
        'SearchCountrySecurity': '',
        'FromDateSubmit': '07/01/2022',
        'ToDateSubmit': '06/30/2023',
        'SortOrder': 1,
        'MeetingID': 0,
        'MeetingFundID': 0,
        'BallotID': 0,
        'RecNum': rec_num,  # Initial value
        'language': 'en',
        'MultipleResults': '',
        'AllMeetingFunds': ''
    }   
    while True:
        # Send the POST request
        response = requests.post(url, data=form_fund)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all <a> elements with class "MeetingListLink"
            meeting_links = soup.find_all('a', class_='MeetingListLink')

            # Check if there are no meeting links
            if not meeting_links:
                print("No meeting links found. Breaking out of the loop.")
                break

            # Extract and print the "href" attribute values
            for link in meeting_links:                
                href_value = link.get('href')                
                match = pattern.search(href_value)
                if match:
                    id_numbers = match.groups()
                    form_detail = {
                        'CustomerID': 1615,
                        'FundID': int(id_numbers[1]),
                        'MeetingListFundID': int(id_numbers[1]),
                        'SingleFund': 0,
                        'FundFamilyID': 0,
                        'SearchType': 1,
                        'AlphaSearch': '',
                        'SearchFor': '',
                        'SearchCountrySecurity': '',
                        'FromDateSubmit': '07/01/2022',
                        'ToDateSubmit': '06/30/2023',
                        'SortOrder': 1,
                        'MeetingID': int(id_numbers[0]),
                        'MeetingFundID': int(id_numbers[1]),
                        'BallotID': int(id_numbers[2]),
                        'RecNum': rec_num,
                        'language': 'en',
                        'MultipleResults': '',
                        'AllMeetingFunds': ''
                    }
                    url_detail = "https://vds.issproxy.com/VoteDetail.php"                
                    # Send the POST request
                    response_detail = requests.post(url_detail, data=form_detail)

                    # Check if the request was successful (status code 200)
                    if response_detail.status_code == 200:
                        # Parse the HTML content with BeautifulSoup
                        soup_detail = BeautifulSoup(response_detail.text, 'html.parser')                        
                        odd_rows = soup_detail.find_all('tr', id='VPDataCol')
                        company_name = soup_detail.find('p', id='VPCompanyNameHeader').get_text().replace('  ', '').replace('\n', '')
                        ticker = soup_detail.find('td', id='VPTicker').get_text().replace('  ', '').replace('\n', '')
                        meeting_date = soup_detail.find('td', id='VPMeetingDate').get_text().replace('  ', '').replace('\n', '')
                        record_date = soup_detail.find('td', id='VPRecordDate').get_text().replace('  ', '').replace('\n', '')
                        security_id = soup_detail.find('td', id='VPSecurity').get_text().replace('  ', '').replace('\n', '')
                        meeting_type = soup_detail.find('td', id='VPMeetingType').get_text().replace('  ', '').replace('\n', '')                        
                        fund_name = soup_detail.find('span', id='VPFundNameNoImage').get_text().replace('  ', '').replace('\n', '').replace('- ', '')                             
                        
                        # Extract and print the inner text of each "td" element
                        for row in odd_rows:
                            item_number_element = row.find('td', id='VPBallotItemNumber')
                            if item_number_element:
                                item_number = item_number_element.get_text().replace('  ', '').replace('\n', '')
                            else:
                                item_number = "N/A"  # or handle the absence of the element in an appropriate way

                            proposal_element = row.find('td', id='VPProposal')
                            if proposal_element:
                                proposal = proposal_element.get_text().replace('  ', '').replace('\n', '')
                            else:
                                proposal = "N/A"

                            mgmt_rec_element = row.find('td', id='VPMgtRecVote')
                            if mgmt_rec_element:
                                mgmt_rec = mgmt_rec_element.get_text().replace('  ', '').replace('\n', '')
                            else:
                                mgmt_rec = "N/A"

                            vote_element = row.find('td', id='VPVoteCast')
                            if vote_element:
                                vote = vote_element.get_text().replace('  ', '').replace('\n', '')
                            else:
                                vote = "N/A"
                            print([company_name, ticker, meeting_date, record_date, security_id, meeting_type, item_number, proposal, mgmt_rec, vote, fund_name])
                            # Append the data to the list
                            data_list.append([company_name, ticker, meeting_date, record_date, security_id, meeting_type, item_number, proposal, mgmt_rec, vote, fund_name])
                    
                    # print(soup_detail)
            
            # Increase RecNum for the next request
            form_fund['RecNum'] += 25
            print(form_fund['RecNum'])
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            print(response.text)
            break  # Break the loop if the response code is not 200
print(data_list)
# Create a DataFrame from the list
df = pd.DataFrame(data_list, columns=['Company Name', 'Ticker', 'Meeting Date', 'Record Date', 'Security ID', 'Meeting Type', 'Item Number', 'Proposal', 'Mgmt Rec', 'Vote', 'Fund'])

# Save the DataFrame to an Excel file
df.to_excel('scraped_data.xlsx', index=False)
