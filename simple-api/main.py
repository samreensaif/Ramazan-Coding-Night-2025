from fastapi import FastAPI
import random

app = FastAPI()

side_hustles = [
    "Freelancing",
    "Web Development",
    "App Development",
    "Graphic Design",
    "UI/UX Design",
    "Content Writing & Blogging",
    "SEO Consulting",
    "Copywriting",
    "Video Editing",
    "Digital Marketing",
    "Dropshipping",
    "Amazon FBA",
    "Print on Demand",
    "Affiliate Marketing",
    "Virtual Assistant",
    "Tech Support & IT Consulting",
    "AI Prompt Engineering",
    "YouTube Channel",
    "TikTok & Instagram Reels",
    "Podcasting",
    "Stock Photography & Videography",
    "Social Media Management",
    "Influencer Marketing",
    "Selling Digital Products",
    "Stock Trading & Investing",
    "Crypto Trading & NFTs",
    "Flipping Websites & Domains",
    "Real Estate Investing",
    "Photography & Videography",
    "Handmade Crafts & Etsy Selling",
    "Calligraphy & Custom Lettering",
    "Tattoo Designing",
    "Home Cleaning Services",
    "Event Planning & Decoration",
    "Pet Sitting & Dog Walking",
    "Car Wash & Detailing",
    "Personal Trainer / Fitness Coaching",
    "Meal Prep & Healthy Food Services",
    "Catering / Home Baking Business",
    "Online Tutoring",
    "Coaching (Fitness, Life, Career, Business)",
    "Music Lessons",
    "Language Translation Services"
]

money_quotes = [
    "Money can't buy happiness, but it's a lot more comfortable to cry in a Mercedes than on a bicycle.",
    "The more you learn, the more you earn. - Warren Buffett",
    "Don't work for money; make money work for you. - Robert Kiyosaki",
    "A penny saved is a penny earned. - Benjamin Franklin",
    "Wealth consists not in having great possessions, but in having few wants. - Epictetus",
    "The rich invest in time, the poor invest in money. - Warren Buffett",
    "Formal education will make you a living; self-education will make you a fortune. - Jim Rohn",
    "If you don’t find a way to make money while you sleep, you will work until you die. - Warren Buffett",
    "Financial freedom is available to those who learn about it and work for it. - Robert Kiyosaki",
    "An investment in knowledge pays the best interest. - Benjamin Franklin",
    "Being rich is having money; being wealthy is having time. - Margaret Bonnano",
    "You must gain control over your money, or the lack of it will forever control you. - Dave Ramsey",
    "Opportunities come infrequently. When it rains gold, put out the bucket, not the thimble. - Warren Buffett",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Do not save what is left after spending, but spend what is left after saving. - Warren Buffett",
    "Rich people stay rich by living like they're broke. Broke people stay broke by living like they're rich.",
    "Never depend on a single income. Make an investment to create a second source. - Warren Buffett",
    "Success is not in what you have, but who you are. - Bo Bennett",
    "It’s not your salary that makes you rich, it’s your spending habits. - Charles A. Jaffe",
    "To get rich, you have to be making money while you're asleep. - David Bailey",
    "Time is money. - Benjamin Franklin",
    "Poor people have big TVs. Rich people have big libraries. - Jim Rohn",
    "Too many people spend money they haven't earned to buy things they don't want to impress people they don't like. - Will Rogers"
]

@app.get("/side_hustles")
def get_side_hustle(apiKey:str):
    """Returns a random side hustle"""
    if apiKey != "1234567":
        return {'error':"invalid API Key"}
    return {'hustle':random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes(apiKey:str):
    """Returns a random money quote"""
    if apiKey != "12345678":
        return {'error':"invalid API Key"}    
    return {"money_quote": random.choice(money_quotes)}