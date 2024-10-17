from flask import Flask

app=Flask(__name__, static_folder= "static1", static_url_path= "/web")

app.run()