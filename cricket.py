from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from datetime import datetime
class ScoreGet:
    def __init__(self):
        """
        Declaring the endpoints, apikey
        """
        self.url_get_all_matches = "http://api.cricapi.com/v1/matches"
        self.url_get_score="http://api.cricapi.com/v1/cricScore"
        self.api_key = "4344be68-5f8c-4a67-9cf6-a2c37d7f792e"
        self.unique_id = ""  # unique to every match
        self.country = "Scotland"

    def get_unique_id(self):
        """
        Returns Indian cricket teams match id, if the match is Live
        :return:
        """
        uri_params = {"apikey": self.api_key}
        resp = requests.get(self.url_get_all_matches, params=uri_params)
        resp_dict = resp.json()
        uid_found=0
        for i in resp_dict['data']:
            if (i['teams'][0] == self.country or i['teams'][1] == self.country) and i['status'] == "Match started":
                todays_date = datetime.today().strftime('%Y-%m-%d')
                if todays_date == i['date'].split("T")[0]:
                    uid_found=1
                    self.unique_id=i['unique_id']
                    print(self.unique_id)
                    break
        if not uid_found:
            self.unique_id=-1
        send_data=self.get_score(self.unique_id)
        return send_data
    def get_score(self,unique_id):
        data="" #stores the cricket match data
        if unique_id == -1:
            data="No India matches today"
        else:
            uri_params = {"apikey": self.api_key, "unique_id": self.unique_id}
            resp=requests.get(self.url_get_score,params=uri_params)
            data_json=resp.json()
            #print(data_json)
            try:
                data="Here's the score : "+ "\n" + data_json['stat'] +'\n' + data_json['score']
            except KeyError as e:
                data="Something went wrong"
        return data

if __name__ == "__main__":
    match_obj=ScoreGet()
    send_message=match_obj.get_unique_id()
    print(send_message)
    from twilio.rest import Client
    account_sid = 'AC8778d07c2281be79d83bfd47adec01d0'
    auth_token = '1c645e781dac6277b694e89474408a71'
    client = Client(account_sid, auth_token)
    message = client.messages.create( body=send_message, from_='whatsapp:+14155238886', to='whatsapp:+919872095303' )