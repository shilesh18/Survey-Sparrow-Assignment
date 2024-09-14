from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .battlecard_generation import generate_battlecard
from .data_collection import get_competitor_data
from .data_analysis import analyze_data
from .battlecard_design import create_battlecard_image

app = FastAPI()

# Add CORS Middleware to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (use specific origins in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "AI-powered Battlecard Generation System"}

@app.post("/generate_battlecard/")
def generate_battlecard_endpoint(competitor_name: str, product_info: str):
    # Step 1: Collect Data
    competitor_data = get_competitor_data(competitor_name)
    
    # Step 2: Analyze Data
    analyzed_data = analyze_data(competitor_data)
    
    # Step 3: Generate Battlecard Content
    battlecard_content = generate_battlecard(analyzed_data, product_info)
    
    # Step 4: Design the Battlecard
    image_path = create_battlecard_image(battlecard_content)
    
    return {"status": "Battlecard generated successfully", "image_path": image_path}
