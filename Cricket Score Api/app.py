from bs4 import BeautifulSoup 
import requests 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/') 
def cricgfg(): 
    html_text = requests.get('https://sports.ndtv.com/cricket/live-scores').text 
    soup = BeautifulSoup(html_text, "html.parser") 
    sect = soup.find_all('div', class_='sp-scr_wrp ind-hig_crd vevent') 

    if sect:
        section = sect[1]
        
        description = section.find('span', class_='description')
        description = description.text if description else 'No description available'
        
        location = section.find('span', class_='location')
        location = location.text if location else 'No location available'
        
        current = section.find('div', class_='scr_dt-red')
        current = current.text if current else 'No current data available'
        
        link_tag = section.find('a', class_='scr_ful-sbr-txt')
        link = "https://sports.ndtv.com/" + link_tag.get('href') if link_tag else 'No link available'
        
    try: 
        status = section.find_all('div', class_="scr_dt-red")[1].text 
        block = section.find_all('div', class_='scr_tm-wrp') 
        team1_block = block[0] 
        team1_name = team1_block.find('div', class_='scr_tm-nm').text 
        team1_score = team1_block.find('span', class_='scr_tm-run').text 
        team2_block = block[1] 
        team2_name = team2_block.find('div', class_='scr_tm-nm').text 
        team2_score = team2_block.find('span', class_='scr_tm-run').text 
        result = { 
                "Description": description, 
                "Location": location, 
                "Status": status, 
                "Current": current, 
                "Team A": team1_name, 
                "Team A Score": team1_score, 
                "Team B": team2_name, 
                "Team B Score": team2_score, 
                "Full Scoreboard": link, 
                "Credits": "NDTV Sports"
            } 
    except:         
        pass
    return jsonify(result)


if __name__ == "__main__": 
    app.run(debug=True) 
    # try:
    #     status = section.find_all('div', class_="scr_dt-red")[1].text if len(section.find_all('div', class_="scr_dt-red")) > 1 else 'No status available'
        
    #     block = section.find_all('div', class_='scr_tm-wrp')
        
    #     if len(block) > 0:
    #         team1_block = block[0]
    #         team1_name = team1_block.find('div', class_='scr_tm-nm')
    #         team1_name = team1_name.text if team1_name else 'No team 1 name available'
            
    #         team1_score = team1_block.find('span', class_='scr_tm-run')
    #         team1_score = team1_score.text if team1_score else 'No team 1 score available'
    #     else:
    #         team1_name = 'No team 1 block available'
    #         team1_score = 'No team 1 score available'
        
    #     if len(block) > 1:
    #         team2_block = block[1]
    #         team2_name = team2_block.find('div', class_='scr_tm-nm')
    #         team2_name = team2_name.text if team2_name else 'No team 2 name available'
            
    #         team2_score = team2_block.find('span', class_='scr_tm-run')
    #         team2_score = team2_score.text if team2_score else 'No team 2 score available'
    #     else:
    #         team2_name = 'No team 2 block available'
    #         team2_score = 'No team 2 score available'
        
    #     print(description.strip()) 
    #     print(location.strip()) 
    #     print(status.strip()) 
    #     print(current.strip()) 
    #     print(team1_name.strip()) 
    #     print(team1_score.strip()) 
    #     print(team2_name.strip()) 
    #     print(team2_score.strip()) 
    #     print(link) 
    # except Exception as e: 
    #     print(f"An error occurred: {e}") 
# else:
#     print("No sections found")
