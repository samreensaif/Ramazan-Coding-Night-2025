from fastapi import FastAPI
import random



app = FastAPI()

random_jokes = [
    {"setup": "Why did the chicken cross the road?","punchline": "To get to the other side!"},
    {"setup": "What do you call a belt made of watches?","punchline": "A waist of time."},
    { "setup": "Doctor: Aap cigarette kyun peetay hain?", "punchline": "Patient: Tension door hoti hai!"},
    { "setup": "Teacher: Beta, Islamabad ka aik aur naam batao?", "punchline": "Student: Load-shedding-abad!"},
    { "setup": "Boy: Agar tum mujhe chhod ke gayi toh main paagal ho jaunga!", "punchline": "Girl: Main ja rahi hoon!"},
    { "setup": "Pathan: Main scientist banna chahta hoon!", "punchline": "Friend: Uske liye research karni hoti hai."},
    { "setup": "Beggar: Bhai koi paisay dey do, 3 din se bhooka hoon!", "punchline": "Man: Toh bhai roza khol le!"},
    {"setup": "Wife: Tum mujhe birthday pe kya gift doge?", "punchline": "Husband: Bijli ka bill bhardoonga!"},
    {"setup": "Customer: Bhai ye doodh kaisa hai?", "punchline": "Doodh wala: Garanteed mineral water mix hai!"},
    {"setup": "Friend: Bhai tu har waqt late kyun hota hai?", "punchline": "Main: Bhai, Pakistani hoon, adat se majboor!"},
    {"setup": "Interviewer: Aapko job kyun chahiye?", "punchline": "Candidate: Kyunki ghar walay kehte hain mobile chhod kar kuch kaam kar lo!"},
    { "setup": "Wife: Main 3 din se tumse baat nahi kar rahi!", "punchline": "Husband: Allah ka shukar, battery charge ho gayi!"},
    { "setup": "Policeman: Tum is waqt raat ko kya kar rahe ho?", "punchline": "Aadmi: Light nahi hai, hawa khanay nikla hoon!"},
    { "setup": "Husband: Mujhe ghar ke kaam nahi karne aate!", "punchline": "Wife: Chalo phir training start karte hain!"},
    { "setup": "Biwi: Tum mujhe pyar nahi karte!", "punchline": "Shohar: Pyar karta hoon lekin bijli ka bill bhi bharna hota hai!"},
    { "setup": "Doctor: Kya masla hai?", "punchline": "Patient: Sir, battery full likha aata hai, phir bhi garmi lagti hai!"},
    { "setup": "Bachay: Abbu, hamari car hybrid hai?", "punchline": "Abbu: Beta, hybrid nahi, load-shedding wali hai!"}
]


        


@app.get("/random-jokes")

def get_random_joke():
    """Get a random joke from the list of jokes"""
    joke = random.choice(random_jokes)
    # return f"{joke['setup']} {joke['punchline']}"
    return joke



