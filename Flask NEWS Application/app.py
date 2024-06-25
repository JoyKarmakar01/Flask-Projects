from flask import Flask, render_template, request
from newsapi import NewsApiClient
import logging

# Init Flask app
app = Flask(__name__)

# Init newsapi
newsapi = NewsApiClient(api_key='70fdb9ba81ba40b6bda148e672898bd9')

# Helper function
def get_sources_and_domains():
    try:
        all_sources = newsapi.get_sources()['sources']
        sources = []
        domains = []
        for e in all_sources:
            id = e['id']
            domain = e['url'].replace("http://", "").replace("https://", "").replace("www.", "")
            slash = domain.find('/')
            if slash != -1:
                domain = domain[:slash]
            sources.append(id)
            domains.append(domain)
        sources = ", ".join(sources)
        domains = ", ".join(domains)
        return sources, domains
    except Exception as e:
        logging.error(f"Error getting sources and domains: {e}")
        return [], []

@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        if request.method == "POST":
            sources, domains = get_sources_and_domains()
            keyword = request.form["keyword"]
            related_news = newsapi.get_everything(q=keyword, sources=sources, domains=domains, language='en', sort_by='relevancy')
            no_of_articles = related_news.get('totalResults', 0)
            if no_of_articles > 100:
                no_of_articles = 100
            all_articles = newsapi.get_everything(q=keyword, sources=sources, domains=domains, language='en', sort_by='relevancy', page_size=no_of_articles).get('articles', [])
            return render_template("home.html", all_articles=all_articles, keyword=keyword)
        else:
            top_headlines = newsapi.get_top_headlines(country="in", language="en")
            total_results = top_headlines.get('totalResults', 0)
            if total_results > 100:
                total_results = 100
            all_headlines = newsapi.get_top_headlines(country="in", page_size=total_results).get('articles', [])
            return render_template("home.html", all_headlines=all_headlines)
    except Exception as e:
        logging.error(f"Error in home route: {e}")
        return render_template("home.html", error="An error occurred while fetching the news. Please try again later.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
