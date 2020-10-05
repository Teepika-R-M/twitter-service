from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)
import tweepy
import config

def connection_establish(app):
    consumer_key = config.consumer_key 

    consumer_secret = config.consumer_secret

    access_token = config.access_token

    access_token_secret = config.access_token_secret 

    auth = tweepy.OAuthHandler(consumer_key,consumer_secret) 
    auth.set_access_token(access_token, access_token_secret) 

    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    @app.route("/")
    def home():
        return render_template("index.html")
    
    @app.route("/threshold", methods=['POST', 'GET'])
    def threshold():
        if request.method == "POST":            
            def generate():
                tweets_id =[]
                tweets_list=[]
                tweets_from_timeline=tweepy.Cursor(api.user_timeline).items()
                for tweets in tweets_from_timeline:
                    tweets_list.append(tweets.text)
                    tweets_id.append(tweets.id)
                return tweets_id,tweets_list
            tvalue = request.form['tvalue']
            if tvalue == "Create a Tweet":
                api.update_status("Test Tweet posted from our tweet-Flask app ")
                return "<html> <center> <h3><br><br><br>Tweet posted</h3> </center> </html>"
            elif tvalue == "Retrieve Tweets":
                tweets_ids,tweets_lists=generate()
                def ulify(elements):
                    string = "<html> <center> <br><h2> Tweets retrieved are </h2> <br><h3><ul>"
                    for s in elements:
                        string += "<li>" + str(s) + "</li>"
                        string += "</ul> </h3></center> </html>"
                        return string
                if not tweets_lists:
                    return "<html> <h3> <center> <br><br><br>No tweets available to retrieve</h3></center> </html> "

                else:
                    html_to_return=ulify(tweets_lists)
                    return html_to_return
            else:
                tweets_ids_delete,tweets_lists_delete=generate()
                api.destroy_status(tweets_ids_delete[0]) 
                return "<html> <center> <h3> <br><br><br> Top tweet deleted </h3> </center> </html>"
        else:
            return "its not a post request"

connection_establish(app)

if __name__ == '__main__':
    app.run(debug=True)
