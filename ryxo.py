from flask import Flask

app = Flask(__name__)

BG = "#05070d"
BLUE = "#2f6bff"
CARD = "#0b1020"

def page_template(title, content):
    return f"""
    <html>
    <head>
        <title>{title} - Ryxo Studios</title>

        <style>
            body {{
                margin: 0;
                font-family: Arial, Helvetica, sans-serif;
                background: {BG};
                color: white;
            }}

            nav {{
                background: black;
                padding: 15px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }}

            nav a {{
                color: {BLUE};
                text-decoration: none;
                margin-left: 20px;
                font-weight: bold;
            }}

            nav a:hover {{
                color: #5aa0ff;
            }}

            .container {{
                padding: 60px;
                text-align: center;
            }}

            .hero {{
                font-size: 48px;
                font-weight: bold;
                color: {BLUE};
            }}

            .card {{
                background: {CARD};
                padding: 25px;
                border-radius: 14px;
                margin: 30px auto;
                width: 70%;
                box-shadow: 0 0 25px rgba(47,107,255,0.25);
            }}

            footer {{
                background: black;
                text-align: center;
                padding: 20px;
                margin-top: 60px;
            }}
        </style>

    </head>

    <body>

        <nav>
            <div style="color:{BLUE}; font-weight:bold;">
                RYXO STUDIOS
            </div>

            <div>
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/credits">Credits</a>   <!-- ✅ Added -->
                <a href="/contact">Contact</a>
            </div>
        </nav>

        {content}

        <footer>
            © 2026 Ryxo Studios — All Rights Reserved
        </footer>

    </body>
    </html>
    """

@app.route("/")
def home():
    content = """
    <div class="container">

        <img class="logo"
        src="https://i.postimg.cc/LXqgJ5kM/Chat-GPT-Image-Feb-7-2026-10-37-34-PM.png">

        <div class="hero">
            Welcome to Ryxo Studios
        </div>

        <div class="card">
            <h2>Next Generation VR Gaming</h2>
            <p>
                This is a VR gaming studio focused on building immersive multiplayer experiences that push the boundaries of what's possible in VR gaming. Our team is dedicated to make the world of VR better, and we are excited to share our journey with you. Join us as we redefine the future of VR gaming.
            </p>
        </div>

    </div>
    """

    return page_template("Home", content)

@app.route("/about")
def about():
    content = """
    <div class="container">
        <div class="hero">About Ryxo</div>
        <div class="card">
            <p>
                Ryxo Studios is focused on high performance VR gaming, building immersive multiplayer experiences that push the boundaries of what's possible in gaming. Our team is dedicated to creating worlds that are rich, dynamic, and full of life, redefining the future of VR gaming.
            </p>
        </div>
    </div>
    """

    return page_template("About", content)

@app.route("/credits")
def credits():
    content = """
    <div class="container">

        <div class="hero">Credits</div>

        <div class="card">
            <h2>Ryxo Studios Team</h2>
            <p>Founder / CEO — Neoswag</p>
            <p>Co-Founder — Koro & Zen</p>
            <p>Lead Developer — Polar</p>
        </div>

        <div class="card">
            <h2>Special Thanks</h2>
            <p>Supporters</p>
            <p>Beta Testers</p>
            <p>Community Members</p>
        </div>

    </div>
    """

    return page_template("Credits", content)

@app.route("/contact")
def contact():
    content = """
    <div class="container">

        <div class="hero">Contact</div>

        <div class="card">
            <p>Email: support@ryxostudios.com</p>
            <p>Discord: Down Below</p>
            <br>
            <button onclick="window.location.href='https://discord.gg/aZrz7QgD5x'">
                Join Community
            </button>
        </div>
    </div>
    """

    return page_template("Contact", content)

if __name__ == "__main__":
    app.run(debug=True)
